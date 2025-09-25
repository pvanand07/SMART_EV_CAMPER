/**
 * AssistantService - Handles communication with the iResearcher API
 */
export class AssistantService {
  constructor(config = {}) {
    this.config = {
      apiUrl: 'https://ev-camper-agent.elevatics.site/api/v1/chat',
      model_id: config.model_id || 'openai/gpt-oss-120b:nitro',
      user_id: config.user_id || this.generateUserId(),
      assistant_mode: true,
      conversation_id: config.conversation_id || this.generateConversationId(),
      ...config
    };
    
    this.onStreamingStart = null;
    this.onStreamingChunk = null;
    this.onStreamingComplete = null;
    this.onTranscriptionReceived = null;
    this.onError = null;
  }

  /**
   * Initialize the assistant service
   * @param {Object} callbacks - Event callbacks
   * @param {Function} callbacks.onStreamingStart - Called when streaming starts
   * @param {Function} callbacks.onStreamingChunk - Called for each chunk of streaming response
   * @param {Function} callbacks.onStreamingComplete - Called when streaming completes
   * @param {Function} callbacks.onTranscriptionReceived - Called when audio transcription is received
   * @param {Function} callbacks.onError - Called when an error occurs
   */
  initialize(callbacks = {}) {
    this.onStreamingStart = callbacks.onStreamingStart;
    this.onStreamingChunk = callbacks.onStreamingChunk;
    this.onStreamingComplete = callbacks.onStreamingComplete;
    this.onTranscriptionReceived = callbacks.onTranscriptionReceived;
    this.onError = callbacks.onError;
  }

  /**
   * Send text query to the assistant
   * @param {string} query - Text query to send
   * @param {Object} options - Additional options
   * @returns {Promise<string>} Complete response text
   */
  async sendTextQuery(query, options = {}) {
    try {
      console.log("Sending text query to API...");
      
      const requestBody = {
        query: query,
        conversation_id: this.config.conversation_id,
        model_id: this.config.model_id,
        user_id: this.config.user_id,
        assistant_mode: true,
        ...options
      };

      console.log("Request config:", requestBody);

      const response = await fetch(this.config.apiUrl, {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestBody)
      });

      console.log("API Response status:", response.status);

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return await this.handleStreamingResponse(response);
    } catch (error) {
      console.error('Text Query API Error:', error);
      if (this.onError) {
        this.onError(error);
      }
      throw error;
    }
  }

  /**
   * Send audio data to the assistant
   * @param {string} audioBase64 - Base64 encoded audio data
   * @param {Object} options - Additional options
   * @returns {Promise<Object>} Object containing transcription and response
   */
  async sendAudioQuery(audioBase64, options = {}) {
    try {
      console.log("🚀 Sending audio query to API...");
      console.log("🚀 Audio data length:", audioBase64.length);
      console.log("🚀 Config:", this.config);
      console.log("🚀 Options:", options);
      
      const requestBody = {
        query: '',
        conversation_id: this.config.conversation_id,
        model_id: this.config.model_id,
        user_id: this.config.user_id,
        assistant_mode: true,
        audio_data: audioBase64,
        ...options
      };

      console.log("🚀 Request body keys:", Object.keys(requestBody));
      console.log("🚀 Request body (without audio_data):", {
        ...requestBody,
        audio_data: `[${audioBase64.length} chars]`
      });

      console.log("🚀 Making fetch request to:", this.config.apiUrl);
      const response = await fetch(this.config.apiUrl, {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestBody)
      });

      console.log("📡 API Response received");
      console.log("📡 Response status:", response.status);
      console.log("📡 Response ok:", response.ok);
      console.log("📡 Response headers:", response.headers);

      if (!response.ok) {
        const errorText = await response.text();
        console.error("❌ API Error response:", errorText);
        throw new Error(`HTTP error! status: ${response.status}, body: ${errorText}`);
      }

      console.log("📡 Starting to handle streaming response...");
      return await this.handleStreamingResponse(response);
    } catch (error) {
      console.error('❌ Audio Query API Error:', error);
      console.error('❌ Error stack:', error.stack);
      if (this.onError) {
        console.log('❌ Calling onError callback');
        this.onError(error);
      } else {
        console.warn('⚠️ No onError callback set');
      }
      throw error;
    }
  }

  /**
   * Handle streaming response from the API
   * @param {Response} response - Fetch response object
   * @returns {Promise<Object>} Object containing transcription and complete response
   */
  async handleStreamingResponse(response) {
    console.log("🔄 Starting to handle streaming response...");
    const reader = response.body.getReader();
    let completeResponse = '';
    let transcribedText = '';

    console.log("📡 Starting to read streaming response...");
    console.log("📡 Reader created:", reader);
    
    if (this.onStreamingStart) {
      console.log("📡 Calling onStreamingStart callback");
      this.onStreamingStart();
    } else {
      console.warn("⚠️ No onStreamingStart callback set");
    }

    try {
      let chunkCount = 0;
      while (true) {
        const { done, value } = await reader.read();
        chunkCount++;
        console.log(`📦 Reading chunk ${chunkCount}, done: ${done}, value length: ${value?.length}`);
        
        if (done) {
          console.log("✅ Streaming complete after", chunkCount, "chunks");
          break;
        }

        const chunk = new TextDecoder().decode(value);
        console.log(`📦 Decoded chunk ${chunkCount}:`, chunk);
        const lines = chunk.split('\n');
        console.log(`📦 Split into ${lines.length} lines:`, lines);

        for (const line of lines) {
          console.log(`🔍 Processing line: "${line}"`);
          if (line.startsWith('data: ') && line !== 'data: ') {
            try {
              const jsonStr = line.substring(6);
              console.log(`🔍 JSON string: "${jsonStr}"`);
              if (jsonStr.trim()) {
                const data = JSON.parse(jsonStr);
                console.log("📋 Parsed data:", data);
                
                if (data.type === 'chunk' && data.content) {
                  completeResponse += data.content;
                  console.log("📝 Added chunk to response. Complete response length:", completeResponse.length);
                  console.log("📝 Chunk content:", data.content);
                  if (this.onStreamingChunk) {
                    console.log("📝 Calling onStreamingChunk callback");
                    this.onStreamingChunk(data.content, completeResponse);
                  } else {
                    console.warn("⚠️ No onStreamingChunk callback set");
                  }
                } else if (data.type === 'transcribed_text' && data.content) {
                  transcribedText = data.content;
                  console.log("📝 Transcribed text received:", transcribedText);
                  if (this.onTranscriptionReceived) {
                    console.log("📝 Calling onTranscriptionReceived callback");
                    this.onTranscriptionReceived(transcribedText);
                  } else {
                    console.warn("⚠️ No onTranscriptionReceived callback set");
                  }
                }
                
                console.log("📋 Processed data:", data);
              }
            } catch (e) {
              console.log("⚠️ Skipping invalid JSON line:", line, "Error:", e.message);
            }
          } else {
            console.log("⏭️ Skipping non-data line:", line);
          }
        }
      }

      console.log("🏁 Calling onStreamingComplete with:", {
        responseLength: completeResponse.length,
        transcriptionLength: transcribedText.length,
        hasCallback: !!this.onStreamingComplete
      });
      
      if (this.onStreamingComplete) {
        console.log("🏁 Calling onStreamingComplete callback");
        this.onStreamingComplete(completeResponse, transcribedText);
      } else {
        console.warn("⚠️ No onStreamingComplete callback set");
      }

      console.log("🏁 Returning final result:", {
        response: completeResponse,
        transcription: transcribedText
      });

      return {
        response: completeResponse,
        transcription: transcribedText
      };

    } catch (error) {
      console.error('Streaming error:', error);
      if (this.onError) {
        this.onError(error);
      }
      throw error;
    }
  }

  /**
   * Update configuration
   * @param {Object} newConfig - New configuration options
   */
  updateConfig(newConfig) {
    this.config = { ...this.config, ...newConfig };
    console.log("Updated config:", this.config);
  }

  /**
   * Reset conversation (generate new conversation ID)
   */
  resetConversation() {
    this.config.conversation_id = this.generateConversationId();
    console.log('New conversation ID:', this.config.conversation_id);
    return this.config.conversation_id;
  }

  /**
   * Get current configuration
   */
  getConfig() {
    return { ...this.config };
  }

  /**
   * Generate a random user ID
   */
  generateUserId() {
    return 'user_' + Math.random().toString(36).substr(2, 9);
  }

  /**
   * Generate a random conversation ID
   */
  generateConversationId() {
    return 'conv_' + Math.random().toString(36).substr(2, 9);
  }

  /**
   * Set API URL
   * @param {string} url - New API URL
   */
  setApiUrl(url) {
    this.config.apiUrl = url;
  }

  /**
   * Set model ID
   * @param {string} modelId - New model ID
   */
  setModelId(modelId) {
    this.config.model_id = modelId;
  }

  /**
   * Get current conversation ID
   */
  getConversationId() {
    return this.config.conversation_id;
  }

  /**
   * Get current user ID
   */
  getUserId() {
    return this.config.user_id;
  }

  /**
   * Release resources and clear callbacks
   */
  release() {
    this.onStreamingStart = null;
    this.onStreamingChunk = null;
    this.onStreamingComplete = null;
    this.onTranscriptionReceived = null;
    this.onError = null;
    console.log("Assistant service resources released");
  }
}

export default AssistantService;
