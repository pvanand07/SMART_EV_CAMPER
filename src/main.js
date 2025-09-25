import { VADService } from './services/VADService.js';
import { AssistantService } from './services/AssistantService.js';
import { TTSService } from './services/TTSService.js';
import './style.css';

/**
 * Main Application Class
 */
class VoiceAssistantApp {
  constructor() {
    this.vadService = new VADService();
    this.assistantService = new AssistantService();
    this.ttsService = new TTSService();
    
    this.isListening = false;
    this.isProcessingAudio = false;
    this.conversationHistory = [];
    this.messageIdCounter = 0;
    
    // DOM elements
    this.elements = {
      micBtn: null,
      statusDiv: null,
      conversationContainer: null,
    };

    this.initializeDOM();
    this.bindEvents();
    this.initializeServices();
  }

  initializeDOM() {
    // Get DOM elements
    this.elements.micBtn = document.getElementById('micBtn');
    this.elements.statusDiv = document.getElementById('status');
    this.elements.conversationContainer = document.getElementById('conversation');

    // Create conversation container if it doesn't exist
    if (!this.elements.conversationContainer) {
      this.elements.conversationContainer = document.createElement('div');
      this.elements.conversationContainer.id = 'conversation';
      this.elements.conversationContainer.className = 'conversation-container';
      document.body.appendChild(this.elements.conversationContainer);
    }

    // Initial UI state
    this.updateUI();
    
    // Initialize Lucide icons
    if (typeof lucide !== 'undefined') {
      lucide.createIcons();
    }
  }

  bindEvents() {
    // Mic button - toggle listening
    this.elements.micBtn?.addEventListener('click', () => this.toggleListening());

    // Handle page unload
    window.addEventListener('beforeunload', () => this.cleanup());
  }

  async initializeServices() {
    try {
      // Initialize VAD service
      await this.vadService.initialize({
        onSpeechStart: () => this.onVADSpeechStart(),
        onSpeechEnd: (audioData) => this.onVADSpeechEnd(audioData),
        onError: (error) => this.onVADError(error)
      });

      // Initialize Assistant service
      this.assistantService.initialize({
        onStreamingStart: () => this.onAssistantStreamingStart(),
        onStreamingChunk: (chunk, completeResponse) => this.onAssistantStreamingChunk(chunk, completeResponse),
        onStreamingComplete: (response, transcription) => this.onAssistantStreamingComplete(response, transcription),
        onTranscriptionReceived: (transcription) => this.onTranscriptionReceived(transcription),
        onError: (error) => this.onAssistantError(error)
      });

      console.log('✅ All services initialized successfully');
      this.updateStatus('Ready - Click microphone to start listening');
    } catch (error) {
      console.error('❌ Error initializing services:', error);
      this.updateStatus(`Initialization error: ${error.message}`);
    }
  }


  async toggleListening() {
    // Always stop all ongoing activities first when mic is pressed
    await this.stopAllActivities();
    
    if (this.isListening) {
      // If currently listening, stop listening
      await this.stopListening();
    } else if (!this.isProcessingAudio) {
      // If not listening and not processing, start listening
      await this.startListening();
    } else {
      // If processing audio, just stop activities and return to default state
      this.resetToDefaultState();
    }
  }

  async startListening() {
    try {
      this.updateStatus('Starting voice detection...');
      this.elements.micBtn?.classList.add('loading');

      // Start VAD immediately (conversation ID maintained throughout session)
      console.log('🎙️ Starting VAD session...');
      await this.vadService.start();
      this.isListening = true;
      
      this.updateUI();

      // Set timeout to stop VAD if no speech detected within 10 seconds
      setTimeout(async () => {
        if (this.isListening && !this.isProcessingAudio) {
          console.log('⏰ VAD timeout - no speech detected');
          await this.stopListening();
        }
      }, 10000);

    } catch (error) {
      console.error('❌ Error starting listening:', error);
      this.updateStatus(`Error: ${error.message}`);
      this.isListening = false;
      this.updateUI();
    }
  }

  async stopListening() {
    try {
      if (this.isListening) {
        await this.vadService.stop();
        this.isListening = false;
        console.log('🛑 VAD stopped');
      }
      
      this.updateUI();

    } catch (error) {
      console.error('❌ Error stopping listening:', error);
      this.updateStatus(`Error: ${error.message}`);
    }
  }


  // VAD Event Handlers
  onVADSpeechStart() {
    console.log('🎤 VAD: Speech started');
    this.updateStatus('Listening to your speech...');
    this.elements.micBtn?.classList.add('recording');
  }

  async onVADSpeechEnd(audioData) {
    console.log('🛑 VAD: Speech ended, processing audio...');
    console.log('🛑 Audio data length:', audioData.length);
    console.log('🛑 Audio data type:', typeof audioData);
    
    this.isProcessingAudio = true;
    this.updateStatus('Processing your speech...');
    
    try {
      // Stop VAD and listening
      await this.stopListening();
      console.log('🛑 VAD stopped successfully');
      
      // Convert audio to base64 WAV
      console.log('🔄 Converting audio to base64...');
      const audioBase64 = VADService.audioToBase64WAV(audioData);
      console.log('✅ Audio converted to base64, length:', audioBase64.length);
      console.log('🔍 Base64 sample (first 100 chars):', audioBase64.substring(0, 100));
      
      // Skip user message - only show assistant response
      console.log('💬 Skipping user message creation - will only show assistant response');
      
      // Send to assistant
      console.log('📡 Sending audio to assistant service...');
      const result = await this.assistantService.sendAudioQuery(audioBase64);
      console.log('📡 Assistant service result:', result);
      
    } catch (error) {
      console.error('❌ Error processing audio:', error);
      console.error('❌ Error stack:', error.stack);
      this.addConversationMessage('assistant', `Sorry, there was an error processing your audio: ${error.message}`);
      // Reset to default state on error
      this.resetToDefaultState();
    }
  }

  onVADError(error) {
    console.error('❌ VAD Error:', error);
    this.updateStatus(`VAD Error: ${error.message}`);
    // Reset to default state after VAD error
    this.resetToDefaultState();
  }

  // Assistant Event Handlers
  onAssistantStreamingStart() {
    console.log('📡 Assistant: Streaming started');
    console.log('📡 Current conversation container:', this.elements.conversationContainer);
    
    // Update status with processing animation
    this.updateStatus('Receiving response...');
    this.elements.statusDiv?.classList.add('processing');
    
    // Update mic button to processing state
    this.elements.micBtn?.classList.remove('loading', 'listening', 'recording', 'detected');
    this.elements.micBtn?.classList.add('processing');
    
    // Create streaming message with typing indicator
    this.currentStreamingMessage = this.addConversationMessage('assistant', this.createTypingIndicator());
    
    // Add streaming animation to the message
    if (this.currentStreamingMessage) {
      this.currentStreamingMessage.classList.add('streaming', 'entering');
      console.log('📡 Added streaming animations to message');
    }
    
    console.log('📡 Created streaming message element:', this.currentStreamingMessage);
  }

  onAssistantStreamingChunk(chunk, completeResponse) {
    console.log('📝 Assistant: Received chunk:', chunk);
    console.log('📝 Complete response so far:', completeResponse);
    console.log('📝 Current streaming message element:', this.currentStreamingMessage);
    
    if (this.currentStreamingMessage) {
      const contentElement = this.currentStreamingMessage.querySelector('.message-content');
      console.log('📝 Content element found:', contentElement);
      if (contentElement) {
        // For streaming, show text with animated cursor
        contentElement.innerHTML = this.escapeHtml(completeResponse) + '<span class="streaming-cursor"></span>';
        console.log('📝 Updated content with streaming cursor:', contentElement.textContent);
        
        // Ensure streaming animation is active
        if (!this.currentStreamingMessage.classList.contains('streaming')) {
          this.currentStreamingMessage.classList.add('streaming');
        }
      } else {
        console.error('❌ No .message-content element found in streaming message');
      }
    } else {
      console.error('❌ No current streaming message available');
    }
  }

  onAssistantStreamingComplete(response, transcription) {
    console.log('✅ Assistant: Streaming complete');
    console.log('✅ Final response:', response);
    console.log('✅ Transcription:', transcription);
    console.log('✅ Current streaming message element:', this.currentStreamingMessage);
    
    // Remove processing status animation
    this.elements.statusDiv?.classList.remove('processing');
    
    if (this.currentStreamingMessage) {
      const contentElement = this.currentStreamingMessage.querySelector('.message-content');
      console.log('✅ Final content element found:', contentElement);
      if (contentElement) {
        // Remove streaming animations and cursor
        this.currentStreamingMessage.classList.remove('streaming');
        
        // Parse markdown for final response
        const parsedContent = this.parseMarkdown(response);
        contentElement.innerHTML = parsedContent;
        console.log('✅ Final content set with markdown parsing:', contentElement.innerHTML);
        
        // Add completion animation
        this.currentStreamingMessage.classList.add('message-complete');
        setTimeout(() => {
          this.currentStreamingMessage?.classList.remove('message-complete');
        }, 1000);
      } else {
        console.error('❌ No .message-content element found for final response');
      }
      
      // Auto-scroll to bottom after streaming is complete
      setTimeout(() => {
        this.currentStreamingMessage.scrollIntoView({ behavior: 'smooth' });
        console.log('📜 Auto-scrolled to bottom after streaming complete');
      }, 100);
      
      this.currentStreamingMessage = null;
    } else {
      console.error('❌ No current streaming message for final response');
      // Fallback: create a new message if streaming message is missing
      console.log('🔄 Creating fallback assistant message');
      this.addConversationMessage('assistant', response);
    }
    
    this.isProcessingAudio = false;
    
    // Auto-play TTS for the assistant response, then reset to default state
    console.log('🔊 Starting TTS playback...');
    this.playAssistantResponseTTS(response);
  }

  onTranscriptionReceived(transcription) {
    console.log('📝 Transcription received:', transcription);
    console.log('📝 User said:', transcription);
    // No need to update UI with transcription since we only show assistant response
    // Just log it for debugging purposes
  }

  onAssistantError(error) {
    console.error('❌ Assistant Error:', error);
    this.addConversationMessage('assistant', `Sorry, there was an error: ${error.message}`);
    this.isProcessingAudio = false;
    
    // Reset to default state after assistant error
    this.resetToDefaultState();
  }

  // Helper Methods
  /**
   * Stop all ongoing activities (TTS, VAD, assistant requests)
   */
  async stopAllActivities() {
    console.log('🛑 Stopping all ongoing activities...');
    
    try {
      // 1. Stop and kill all TTS immediately
      console.log('🔇 Stopping all TTS...');
      this.ttsService.stopAllTTS();
      
      // 2. Stop VAD if active
      if (this.isListening) {
        console.log('🛑 Stopping VAD...');
        await this.vadService.stop();
      }
      
      // 3. Cancel any ongoing assistant requests
      // Note: We don't reset conversation ID, just stop current streaming
      console.log('❌ Stopping any ongoing assistant requests...');
      
      // 4. Clear streaming message if active
      if (this.currentStreamingMessage) {
        console.log('🧹 Clearing streaming message...');
        this.currentStreamingMessage = null;
      }
      
      console.log('✅ All activities stopped');
    } catch (error) {
      console.error('❌ Error stopping activities:', error);
    }
  }

  /**
   * Reset to default state (mic button off, ready to listen)
   */
  resetToDefaultState() {
    console.log('🔄 Resetting to default state...');
    
    // Reset all flags
    this.isListening = false;
    this.isProcessingAudio = false;
    
    // Remove processing animations
    this.elements.statusDiv?.classList.remove('processing');
    this.elements.micBtn?.classList.remove('processing');
    
    // Update UI to default state
    this.updateUI();
    
    console.log('✅ Reset to default state complete');
  }

  /**
   * Play TTS for assistant response, then reset to default state
   * @param {string} response - The assistant's text response
   */
  async playAssistantResponseTTS(response) {
    if (!response || response.trim() === '') {
      console.warn('⚠️ No response text to convert to speech');
      this.resetToDefaultState();
      return;
    }

    try {
      // Generate unique ID for this TTS instance
      this.messageIdCounter++;
      const ttsId = `assistant_msg_${this.messageIdCounter}`;
      
      console.log('🔊 Starting TTS for assistant response...');
      this.updateStatus('Playing response audio...');
      
      // Auto-play TTS with callbacks
      await this.ttsService.autoPlayTTS(ttsId, response, {
        voice: 'af_bella',
        model: 'hexgrad/Kokoro-82M'
      });
      
      // Reset to default state after TTS completes
      this.resetToDefaultState();
      
    } catch (error) {
      console.error('❌ TTS Error:', error);
      // Reset to default state even on TTS error
      this.resetToDefaultState();
    }
  }


  addConversationMessage(type, content) {
    console.log('💬 Adding conversation message:', { type, content });
    console.log('💬 Conversation container exists:', !!this.elements.conversationContainer);
    
    if (!this.elements.conversationContainer) {
      console.error('❌ No conversation container found!');
      return null;
    }
    
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${type}`;
    
    // Parse markdown content
    const parsedContent = this.parseMarkdown(content);
    
    // For assistant messages, only show content without header/timestamp
    let messageHTML;
    if (type === 'assistant') {
      messageHTML = `<div class="message-content">${parsedContent}</div>`;
    } else {
      // Keep header for user messages (if any are shown)
      const timestamp = new Date().toLocaleTimeString();
      messageHTML = `
        <div class="message-header">
          <strong>${type === 'user' ? 'You' : 'Assistant'}</strong>
          <span class="message-time">${timestamp}</span>
        </div>
        <div class="message-content">${parsedContent}</div>
      `;
    }
    
    console.log('💬 Message HTML:', messageHTML);
    messageDiv.innerHTML = messageHTML;
    
    console.log('💬 Created message div:', messageDiv);
    console.log('💬 Message div classes:', messageDiv.className);
    
    this.elements.conversationContainer.appendChild(messageDiv);
    console.log('💬 Appended message to container');
    console.log('💬 Container children count:', this.elements.conversationContainer.children.length);
    
    // Auto-scroll to bottom
    setTimeout(() => {
      messageDiv.scrollIntoView({ behavior: 'smooth' });
      console.log('💬 Scrolled to message');
    }, 100);
    
    return messageDiv;
  }

  /**
   * Create a typing indicator for the assistant message
   * @returns {string} - HTML string for typing indicator
   */
  createTypingIndicator() {
    return '<div class="typing-indicator"><div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div></div>';
  }

  /**
   * Escape HTML characters to prevent XSS
   * @param {string} text - Text to escape
   * @returns {string} - Escaped HTML string
   */
  escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  /**
   * Parse markdown content safely
   * @param {string} content - Raw text content that may contain markdown
   * @returns {string} - HTML string with parsed markdown
   */
  parseMarkdown(content) {
    if (!content) return '';
    
    try {
      // Check if marked library is available
      if (typeof marked !== 'undefined') {
        // Configure marked for safe rendering
        marked.setOptions({
          breaks: true, // Convert line breaks to <br>
          gfm: true,    // Enable GitHub Flavored Markdown
          sanitize: false, // We'll handle sanitization
          smartLists: true,
          smartypants: true
        });
        
        // Parse markdown to HTML
        const htmlContent = marked.parse(content);
        console.log('✅ Markdown parsed successfully');
        return htmlContent;
      } else {
        console.warn('⚠️ Marked library not available, returning plain text');
        return content.replace(/\n/g, '<br>');
      }
    } catch (error) {
      console.error('❌ Error parsing markdown:', error);
      // Fallback to plain text with line breaks
      return content.replace(/\n/g, '<br>');
    }
  }

  clearConversation() {
    console.log('🧹 Clearing conversation UI...');
    if (this.elements.conversationContainer) {
      console.log('🧹 Clearing', this.elements.conversationContainer.children.length, 'messages');
      this.elements.conversationContainer.innerHTML = '';
      console.log('🧹 Conversation UI cleared');
    } else {
      console.warn('⚠️ No conversation container to clear');
    }
    this.conversationHistory = [];
  }

  resetConversation() {
    console.log('🔄 Resetting conversation ID...');
    this.assistantService.resetConversation();
    this.clearConversation();
    console.log('✅ Conversation ID reset');
  }


  updateStatus(message) {
    if (this.elements.statusDiv) {
      this.elements.statusDiv.textContent = message;
    }
  }

  async updateUI() {
    // Update button state
    if (this.elements.micBtn) {
      // Clear all state classes first
      this.elements.micBtn.classList.remove('loading', 'listening', 'recording', 'detected', 'processing');
      
      if (this.isProcessingAudio) {
        this.elements.micBtn.classList.add('processing');
        this.updateStatus('Processing...');
        this.elements.statusDiv?.classList.add('processing');
      } else if (this.isListening) {
        this.elements.micBtn.classList.add('listening');
        this.updateStatus('Listening for speech...');
        this.elements.statusDiv?.classList.remove('processing');
      } else {
        this.updateStatus('Click microphone to start listening');
        this.elements.statusDiv?.classList.remove('processing');
      }
    }
  }

  async cleanup() {
    try {
      if (this.isListening) {
        await this.stopListening();
      }
      
      if (this.ttsService) {
        this.ttsService.cleanup();
      }
      
      if (this.vadService) {
        this.vadService.release();
      }
      
      if (this.assistantService) {
        this.assistantService.release();
      }
      
      console.log('🧹 All services cleaned up');
    } catch (error) {
      console.error('❌ Error during cleanup:', error);
    }
  }
}

// Initialize the app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new VoiceAssistantApp();
});

// Handle hot reload in development
if (import.meta.hot) {
  import.meta.hot.accept();
}

