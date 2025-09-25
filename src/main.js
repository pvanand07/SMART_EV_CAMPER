import { PorcupineService } from './services/PorcupineService.js';
import { VADService } from './services/VADService.js';
import { AssistantService } from './services/AssistantService.js';
import { TTSService } from './services/TTSService.js';
import './style.css';

/**
 * Main Application Class
 */
class WakeWordApp {
  constructor() {
    this.porcupineService = new PorcupineService();
    this.vadService = new VADService();
    this.assistantService = new AssistantService();
    this.ttsService = new TTSService();
    
    this.isListening = false;
    this.isVADActive = false;
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
    } catch (error) {
      console.error('❌ Error initializing services:', error);
      this.updateStatus(`Initialization error: ${error.message}`);
    }
  }


  async toggleListening() {
    if (this.isListening) {
      await this.stopListening();
    } else {
      await this.startListening();
    }
  }

  async startListening() {
    try {
      this.updateStatus('Initializing...');
      this.elements.micBtn?.classList.add('loading');

      // Reset conversation when mic is turned on (not on every wake word)
      this.assistantService.resetConversation();
      console.log('🔄 Conversation reset on mic start');

      // Initialize Porcupine (access key and microphone permission handled automatically)
      await this.porcupineService.initialize(
        (detection) => this.onKeywordDetected(detection),
        (error) => this.onError(error)
      );

      // Start listening
      await this.porcupineService.startListening();
      
      this.isListening = true;
      this.updateUI();

    } catch (error) {
      this.updateStatus(`Error: ${error.message}`);
      this.isListening = false;
      this.updateUI();
    }
  }

  async stopListening() {
    try {
      await this.porcupineService.stopListening();
      
      this.isListening = false;
      this.updateUI();

    } catch (error) {
      this.updateStatus(`Error: ${error.message}`);
    }
  }

  async onKeywordDetected(detection) {
    console.log(`🎯 Wake word "${detection.label}" detected! Killing all resources and clearing everything...`);
    
    try {
      // AGGRESSIVE RESOURCE CLEANUP - Kill everything immediately
      console.log('🧹 Performing aggressive resource cleanup...');
      
      // 1. Stop and kill all TTS immediately
      console.log('🔇 Killing all TTS...');
      this.ttsService.stopAllTTS();
      this.ttsService.cleanup();
      
      // 2. Force stop any ongoing VAD session
      if (this.isVADActive) {
        console.log('🛑 Force stopping VAD...');
        await this.stopVAD();
      }
      
      // 3. Cancel any ongoing assistant requests
      console.log('❌ Cancelling assistant requests...');
      if (this.assistantService) {
        // Reset assistant service to cancel any ongoing requests
        this.assistantService.resetConversation();
      }
      
      // 4. Reset all processing flags
      this.isProcessingAudio = false;
      this.isVADActive = false;
      
      // 5. Clear all conversation data and UI
      console.log('🧹 Clearing all conversation data...');
      this.clearConversation();
      this.conversationHistory = [];
      this.messageIdCounter = 0;
      this.currentStreamingMessage = null;
      
      // 6. Clear any pending timeouts/intervals
      // Note: Individual services should handle their own timeout cleanup
      
      // Visual feedback for wake word detection
      this.elements.micBtn?.classList.remove('listening', 'recording');
      this.elements.micBtn?.classList.add('detected');
      this.updateStatus(`Please speak now...`);
      
      // 7. Temporarily pause wake word detection during VAD to avoid conflicts
      console.log('⏸️ Temporarily pausing wake word detection for new VAD session...');
      await this.porcupineService.stopListening();
      
      // 8. Start fresh VAD session
      console.log('🎙️ Starting fresh VAD session...');
      await this.vadService.start();
      this.isVADActive = true;
      
      // Set timeout to stop VAD if no speech detected within 10 seconds
      setTimeout(async () => {
        if (this.isVADActive && !this.isProcessingAudio) {
          console.log('⏰ VAD timeout - no speech detected');
          await this.stopVAD();
          // Resume wake word listening after timeout
          await this.resumeWakeWordListening();
          this.updateStatus('No speech detected. Listening for "Hey Compass"...');
          this.returnToListeningState();
        }
      }, 10000);
      
      console.log('✅ All resources cleared and killed successfully');
      
    } catch (error) {
      console.error('❌ Error during resource cleanup after wake word:', error);
      this.updateStatus(`Error: ${error.message}`);
      
      // Emergency recovery - try to resume wake word listening
      try {
        await this.resumeWakeWordListening();
        this.returnToListeningState();
      } catch (resumeError) {
        console.error('❌ Failed to resume after cleanup error:', resumeError);
        this.returnToListeningState();
      }
    }
  }

  onError(error) {
    this.updateStatus(`Error: ${error.message}`);
    this.isListening = false;
    this.updateUI();
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
      // Stop VAD
      await this.stopVAD();
      console.log('🛑 VAD stopped successfully');
      
      // Resume wake word listening immediately after VAD ends
      await this.resumeWakeWordListening();
      
      // Return to listening state immediately after VAD ends (mic goes back to blue)
      this.returnToListeningState();
      
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
      // Ensure wake word listening is resumed even on error
      await this.resumeWakeWordListening();
      this.returnToListeningState();
    }
  }

  onVADError(error) {
    console.error('❌ VAD Error:', error);
    this.updateStatus(`VAD Error: ${error.message}`);
    // Resume wake word listening after VAD error
    this.resumeWakeWordListening().then(() => {
      this.returnToListeningState();
    }).catch(resumeError => {
      console.error('❌ Failed to resume wake word listening after VAD error:', resumeError);
      this.returnToListeningState();
    });
  }

  // Assistant Event Handlers
  onAssistantStreamingStart() {
    console.log('📡 Assistant: Streaming started');
    console.log('📡 Current conversation container:', this.elements.conversationContainer);
    this.updateStatus('Receiving response...');
    this.currentStreamingMessage = this.addConversationMessage('assistant', '');
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
        contentElement.textContent = completeResponse + '|';
        console.log('📝 Updated content:', contentElement.textContent);
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
    
    if (this.currentStreamingMessage) {
      const contentElement = this.currentStreamingMessage.querySelector('.message-content');
      console.log('✅ Final content element found:', contentElement);
      if (contentElement) {
        contentElement.textContent = response;
        console.log('✅ Final content set:', contentElement.textContent);
      } else {
        console.error('❌ No .message-content element found for final response');
      }
      this.currentStreamingMessage = null;
    } else {
      console.error('❌ No current streaming message for final response');
      // Fallback: create a new message if streaming message is missing
      console.log('🔄 Creating fallback assistant message');
      this.addConversationMessage('assistant', response);
    }
    
    this.isProcessingAudio = false;
    
    // Auto-play TTS for the assistant response (wake word remains active during TTS)
    console.log('🔊 Starting TTS playback (wake word detection remains active)...');
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
    
    // Ensure wake word listening is resumed even after assistant errors
    this.resumeWakeWordListening().then(() => {
      this.returnToListeningState();
    }).catch(resumeError => {
      console.error('❌ Failed to resume wake word listening after assistant error:', resumeError);
      this.returnToListeningState();
    });
  }

  // Helper Methods
  async stopVAD() {
    if (this.isVADActive) {
      await this.vadService.stop();
      this.isVADActive = false;
      console.log('🛑 VAD stopped');
    }
  }

  /**
   * Resume wake word listening after VAD ends
   */
  async resumeWakeWordListening() {
    if (!this.isListening) {
      console.log('⚠️ Not in listening mode, skipping wake word resume');
      return;
    }

    try {
      console.log('▶️ Resuming wake word detection...');
      await this.porcupineService.startListening();
      console.log('✅ Wake word detection resumed successfully');
    } catch (error) {
      console.error('❌ Failed to resume wake word listening:', error);
      throw error;
    }
  }

  /**
   * Play TTS for assistant response
   * Note: Wake word detection remains active during TTS playback and can interrupt it
   * @param {string} response - The assistant's text response
   */
  async playAssistantResponseTTS(response) {
    if (!response || response.trim() === '') {
      console.warn('⚠️ No response text to convert to speech');
      return;
    }

    try {
      // Generate unique ID for this TTS instance
      this.messageIdCounter++;
      const ttsId = `assistant_msg_${this.messageIdCounter}`;
      
      console.log('🔊 Starting TTS for assistant response (wake word detection active)...');
      this.updateStatus('Playing response audio...');
      
      // Auto-play TTS with callbacks
      // Wake word detection continues during TTS and will interrupt if detected
      await this.ttsService.autoPlayTTS(ttsId, response, {
        voice: 'af_bella',
        model: 'hexgrad/Kokoro-82M'
      });
      
    } catch (error) {
      console.error('❌ TTS Error:', error);
      // Don't show error to user, just log it - the text response is still visible
    }
  }

  returnToListeningState() {
    this.elements.micBtn?.classList.remove('detected', 'recording');
    if (this.isListening) {
      this.elements.micBtn?.classList.add('listening');
      this.updateStatus('Listening for "Hey Compass"...');
      
      // Ensure wake word listening is active (defensive programming)
      this.ensureWakeWordListening();
    }
  }

  /**
   * Ensure wake word listening is active (defensive check)
   */
  async ensureWakeWordListening() {
    try {
      const status = this.porcupineService.getStatus();
      if (this.isListening && !status.isListening) {
        console.log('🔧 Wake word not listening, restarting...');
        await this.resumeWakeWordListening();
      }
    } catch (error) {
      console.error('❌ Error ensuring wake word listening:', error);
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
    
    // For assistant messages, only show content without header/timestamp
    let messageHTML;
    if (type === 'assistant') {
      messageHTML = `<div class="message-content">${content}</div>`;
    } else {
      // Keep header for user messages (if any are shown)
      const timestamp = new Date().toLocaleTimeString();
      messageHTML = `
        <div class="message-header">
          <strong>${type === 'user' ? 'You' : 'Assistant'}</strong>
          <span class="message-time">${timestamp}</span>
        </div>
        <div class="message-content">${content}</div>
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

  clearConversation() {
    console.log('🧹 Clearing conversation...');
    if (this.elements.conversationContainer) {
      console.log('🧹 Clearing', this.elements.conversationContainer.children.length, 'messages');
      this.elements.conversationContainer.innerHTML = '';
      console.log('🧹 Conversation cleared');
    } else {
      console.warn('⚠️ No conversation container to clear');
    }
    this.conversationHistory = [];
  }


  updateStatus(message) {
    if (this.elements.statusDiv) {
      this.elements.statusDiv.textContent = message;
    }
  }

  async updateUI() {
    // Update button state
    if (this.elements.micBtn) {
      this.elements.micBtn.classList.remove('loading');
      
      if (this.isListening) {
        this.elements.micBtn.classList.add('listening');
        this.updateStatus('Listening...');
      } else {
        this.elements.micBtn.classList.remove('listening');
        this.updateStatus('Tap to start listening');
      }
    }
  }

  async cleanup() {
    try {
      if (this.isVADActive) {
        await this.stopVAD();
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
      
      if (this.porcupineService) {
        await this.porcupineService.release();
      }
      
      console.log('🧹 All services cleaned up');
    } catch (error) {
      console.error('❌ Error during cleanup:', error);
    }
  }
}

// Initialize the app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new WakeWordApp();
});

// Handle hot reload in development
if (import.meta.hot) {
  import.meta.hot.accept();
}

