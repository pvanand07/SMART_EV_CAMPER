/**
 * VADService - Voice Activity Detection service using @ricky0123/vad-web
 */
export class VADService {
  constructor() {
    this.myvad = null;
    this.isStarted = false;
    this.isListening = false;
    this.onSpeechStart = null;
    this.onSpeechEnd = null;
    this.onError = null;
  }

  /**
   * Initialize VAD service
   * @param {Object} callbacks - Callback functions
   * @param {Function} callbacks.onSpeechStart - Called when speech starts
   * @param {Function} callbacks.onSpeechEnd - Called when speech ends with audio data
   * @param {Function} callbacks.onError - Called when error occurs
   */
  async initialize(callbacks = {}) {
    this.onSpeechStart = callbacks.onSpeechStart;
    this.onSpeechEnd = callbacks.onSpeechEnd;
    this.onError = callbacks.onError;
  }

  /**
   * Start VAD listening
   */
  async start() {
    try {
      console.log("Starting VAD...");
      
      // Check if vad library is available
      if (typeof vad === 'undefined') {
        throw new Error('VAD library not loaded. Make sure to include @ricky0123/vad-web');
      }

      this.myvad = await vad.MicVAD.new({
        onSpeechStart: () => {
          console.log("Speech start detected");
          this.isListening = true;
          if (this.onSpeechStart) {
            this.onSpeechStart();
          }
        },
        onSpeechEnd: (audio) => {
          console.log("Speech end detected, audio length:", audio.length);
          this.isListening = false;
          if (this.onSpeechEnd) {
            this.onSpeechEnd(audio);
          }
        }
      });
      
      await this.myvad.start();
      this.isStarted = true;
      console.log("VAD started successfully");
      return true;
    } catch (error) {
      console.error("Error starting VAD:", error);
      if (this.onError) {
        this.onError(error);
      }
      throw error;
    }
  }

  /**
   * Stop VAD listening
   */
  async stop() {
    if (this.myvad && this.isStarted) {
      this.myvad.pause();
      this.isStarted = false;
      this.isListening = false;
      console.log("VAD stopped");
    }
  }

  /**
   * Check if VAD is currently started
   */
  isVADStarted() {
    return this.isStarted;
  }

  /**
   * Check if currently listening for speech
   */
  isCurrentlyListening() {
    return this.isListening;
  }

  /**
   * Get current status
   */
  getStatus() {
    return {
      isStarted: this.isStarted,
      isListening: this.isListening
    };
  }

  /**
   * Convert Float32Array audio data to base64 WAV format
   * @param {Float32Array} audioData - Raw audio data
   * @returns {string} Base64 encoded WAV data
   */
  static audioToBase64WAV(audioData) {
    // Create WAV file from Float32Array
    const sampleRate = 16000;
    const numChannels = 1;
    const bitsPerSample = 16;
    
    const length = audioData.length;
    const arrayBuffer = new ArrayBuffer(44 + length * 2);
    const view = new DataView(arrayBuffer);
    
    // WAV header
    const writeString = (offset, string) => {
      for (let i = 0; i < string.length; i++) {
        view.setUint8(offset + i, string.charCodeAt(i));
      }
    };
    
    writeString(0, 'RIFF');
    view.setUint32(4, 36 + length * 2, true);
    writeString(8, 'WAVE');
    writeString(12, 'fmt ');
    view.setUint32(16, 16, true);
    view.setUint16(20, 1, true);
    view.setUint16(22, numChannels, true);
    view.setUint32(24, sampleRate, true);
    view.setUint32(28, sampleRate * numChannels * bitsPerSample / 8, true);
    view.setUint16(32, numChannels * bitsPerSample / 8, true);
    view.setUint16(34, bitsPerSample, true);
    writeString(36, 'data');
    view.setUint32(40, length * 2, true);
    
    // Convert float samples to 16-bit PCM
    let offset = 44;
    for (let i = 0; i < length; i++) {
      const sample = Math.max(-1, Math.min(1, audioData[i]));
      view.setInt16(offset, sample * 0x7FFF, true);
      offset += 2;
    }
    
    // Convert to base64
    const bytes = new Uint8Array(arrayBuffer);
    let binary = '';
    for (let i = 0; i < bytes.byteLength; i++) {
      binary += String.fromCharCode(bytes[i]);
    }
    return btoa(binary);
  }

  /**
   * Release resources
   */
  release() {
    if (this.myvad) {
      this.stop();
      this.myvad = null;
    }
    this.onSpeechStart = null;
    this.onSpeechEnd = null;
    this.onError = null;
    console.log("VAD resources released");
  }
}

export default VADService;
