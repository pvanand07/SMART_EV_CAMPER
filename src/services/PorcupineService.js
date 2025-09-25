import { PorcupineWorker } from "@picovoice/porcupine-web";
import { WebVoiceProcessor } from "@picovoice/web-voice-processor";

/**
 * PorcupineService - Handles wake word detection using Picovoice Porcupine
 */
export class PorcupineService {
  constructor() {
    this.porcupine = null;
    this.isInitialized = false;
    this.isListening = false;
    this.onKeywordDetected = null;
    this.onError = null;
    // Hardcoded access key
    this.accessKey = 'ccP5SRnuSF94N5+f0Vk922F5kzqfnQ2xJpibZGVGU4FubdIavYsvzA==';
  }

  /**
   * Initialize Porcupine with custom keyword model
   * @param {Function} keywordCallback - Callback function when keyword is detected
   * @param {Function} errorCallback - Callback function for errors
   */
  async initialize(keywordCallback = null, errorCallback = null) {
    try {
      // Auto-request microphone permission
      const hasPermission = await PorcupineService.requestMicrophonePermission();
      if (!hasPermission) {
        throw new Error('Microphone permission is required for wake word detection');
      }

      this.onKeywordDetected = keywordCallback;
      this.onError = errorCallback;

      // Define the custom keyword model
      const keywordModel = {
        publicPath: "/Hey-Compass_en_wasm_v3_0_0.ppn", // Path to your .ppn file in public directory
        label: "Hey Compass", // Label for the custom keyword
      };

      // Keyword detection callback
      const detectionCallback = (detection) => {
        console.log(`🎯 Porcupine detected keyword: "${detection.label}"`);
        if (this.onKeywordDetected) {
          this.onKeywordDetected(detection);
        }
      };

      // Create Porcupine worker with custom keyword using hardcoded access key
      this.porcupine = await PorcupineWorker.create(
        this.accessKey,
        [keywordModel], // Array of keyword models
        detectionCallback,
        {
          publicPath: "/porcupine_params.pv", // Path to your .pv model file in public directory
        }
      );

      this.isInitialized = true;
      console.log("✅ Porcupine initialized successfully");
      return true;

    } catch (error) {
      console.error("❌ Failed to initialize Porcupine:", error);
      if (this.onError) {
        this.onError(error);
      }
      throw error;
    }
  }

  /**
   * Start listening for wake word
   */
  async startListening() {
    if (!this.isInitialized) {
      throw new Error("Porcupine not initialized. Call initialize() first.");
    }

    if (this.isListening) {
      console.log("⚠️ Already listening");
      return;
    }

    try {
      await WebVoiceProcessor.subscribe(this.porcupine);
      this.isListening = true;
      console.log("🎤 Started listening for wake word...");
    } catch (error) {
      console.error("❌ Failed to start listening:", error);
      if (this.onError) {
        this.onError(error);
      }
      throw error;
    }
  }

  /**
   * Stop listening for wake word
   */
  async stopListening() {
    if (!this.isListening) {
      console.log("⚠️ Not currently listening");
      return;
    }

    try {
      await WebVoiceProcessor.unsubscribe(this.porcupine);
      this.isListening = false;
      console.log("🛑 Stopped listening for wake word");
    } catch (error) {
      console.error("❌ Failed to stop listening:", error);
      if (this.onError) {
        this.onError(error);
      }
      throw error;
    }
  }

  /**
   * Release all resources
   */
  async release() {
    try {
      if (this.isListening) {
        await this.stopListening();
      }

      if (this.porcupine) {
        this.porcupine.release();
        this.porcupine.terminate();
        this.porcupine = null;
      }

      this.isInitialized = false;
      console.log("🧹 Porcupine resources released");
    } catch (error) {
      console.error("❌ Error releasing resources:", error);
      if (this.onError) {
        this.onError(error);
      }
    }
  }

  /**
   * Get current status
   */
  getStatus() {
    return {
      isInitialized: this.isInitialized,
      isListening: this.isListening,
    };
  }

  /**
   * Check if microphone permission is granted
   */
  static async checkMicrophonePermission() {
    try {
      const result = await navigator.permissions.query({ name: 'microphone' });
      return result.state === 'granted';
    } catch (error) {
      console.warn("Could not check microphone permission:", error);
      return false;
    }
  }

  /**
   * Request microphone permission
   */
  static async requestMicrophonePermission() {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      // Stop the stream immediately, we just needed permission
      stream.getTracks().forEach(track => track.stop());
      return true;
    } catch (error) {
      console.error("Microphone permission denied:", error);
      return false;
    }
  }
}

export default PorcupineService;
