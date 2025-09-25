/**
 * Text-to-Speech Service
 * Handles TTS generation, audio playback, and state management
 */
export class TTSService {
    constructor(baseUrl = 'https://ev-camper-agent.elevatics.site') {
        this.baseUrl = baseUrl;
        this.activeAudio = new Map(); // Store active audio instances
        this.audioUrls = new Set(); // Track created URLs for cleanup
    }

    /**
     * Generate TTS audio from text
     * @param {string} text - Text to convert to speech
     * @param {string} voice - Voice ID (default: 'af_bella')
     * @param {string} model - TTS model (default: 'hexgrad/Kokoro-82M')
     * @returns {Promise<{audio: Audio, url: string}>} Audio element and blob URL
     */
    async generateTTS(text, voice = 'af_bella', model = 'hexgrad/Kokoro-82M') {
        try {
            console.log('🔊 Generating TTS for:', text.substring(0, 100) + '...');
            
            const response = await fetch(`${this.baseUrl}/api/v1/tts`, {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    text: text,
                    voice: voice,
                    model: model
                })
            });

            if (!response.ok) {
                throw new Error(`TTS API error: ${response.status} - ${response.statusText}`);
            }

            // Get audio blob
            const audioBlob = await response.blob();
            const audioUrl = URL.createObjectURL(audioBlob);
            
            // Track URL for cleanup
            this.audioUrls.add(audioUrl);
            
            // Create audio element
            const audio = new Audio(audioUrl);
            
            console.log('✅ TTS generated successfully');
            return { audio, url: audioUrl };
        } catch (error) {
            console.error('❌ TTS Generation Error:', error);
            throw error;
        }
    }

    /**
     * Play TTS audio with automatic state management
     * @param {string} id - Unique identifier for this TTS instance
     * @param {string} text - Text to convert to speech
     * @param {Object} options - TTS options
     * @param {Function} onPlay - Callback when audio starts playing
     * @param {Function} onEnd - Callback when audio ends
     * @param {Function} onError - Callback when error occurs
     * @returns {Promise<void>}
     */
    async playTTS(id, text, options = {}, onPlay = null, onEnd = null, onError = null) {
        try {
            console.log('🔊 Playing TTS for ID:', id);
            
            // Stop any existing audio for this ID
            this.stopTTS(id);

            // Generate new TTS
            const { audio, url } = await this.generateTTS(
                text, 
                options.voice || 'af_bella',
                options.model || 'hexgrad/Kokoro-82M'
            );

            // Set up event handlers
            audio.addEventListener('play', () => {
                console.log('▶️ TTS started playing for:', id);
                if (onPlay) onPlay();
            });

            audio.addEventListener('ended', () => {
                console.log('⏹️ TTS finished playing for:', id);
                this.cleanupAudio(id);
                if (onEnd) onEnd();
            });

            audio.addEventListener('error', (error) => {
                console.error(`❌ TTS Audio Error for ${id}:`, error);
                this.cleanupAudio(id);
                if (onError) onError(error);
            });

            // Store audio instance
            this.activeAudio.set(id, { audio, url, isPlaying: true });

            // Play audio
            await audio.play();

        } catch (error) {
            console.error(`❌ TTS Play Error for ${id}:`, error);
            if (onError) onError(error);
        }
    }

    /**
     * Pause TTS audio
     * @param {string} id - TTS instance identifier
     */
    pauseTTS(id) {
        const instance = this.activeAudio.get(id);
        if (instance && instance.audio && instance.isPlaying) {
            instance.audio.pause();
            instance.isPlaying = false;
            console.log('⏸️ TTS paused for:', id);
        }
    }

    /**
     * Resume paused TTS audio
     * @param {string} id - TTS instance identifier
     */
    resumeTTS(id) {
        const instance = this.activeAudio.get(id);
        if (instance && instance.audio && !instance.isPlaying) {
            instance.audio.play().then(() => {
                instance.isPlaying = true;
                console.log('▶️ TTS resumed for:', id);
            }).catch(error => {
                console.error(`❌ TTS Resume Error for ${id}:`, error);
            });
        }
    }

    /**
     * Stop TTS audio completely
     * @param {string} id - TTS instance identifier
     */
    stopTTS(id) {
        const instance = this.activeAudio.get(id);
        if (instance) {
            if (instance.audio) {
                instance.audio.pause();
                instance.audio.currentTime = 0;
            }
            this.cleanupAudio(id);
            console.log('⏹️ TTS stopped for:', id);
        }
    }

    /**
     * Toggle TTS playback (play/pause)
     * @param {string} id - TTS instance identifier
     * @param {string} text - Text for initial play (if not already generated)
     * @param {Object} options - TTS options
     * @param {Object} callbacks - Event callbacks {onPlay, onEnd, onError}
     * @returns {Promise<string>} Current state: 'playing', 'paused', or 'stopped'
     */
    async toggleTTS(id, text = '', options = {}, callbacks = {}) {
        const instance = this.activeAudio.get(id);
        
        if (!instance) {
            // No audio exists, create and play
            await this.playTTS(id, text, options, callbacks.onPlay, callbacks.onEnd, callbacks.onError);
            return 'playing';
        } else if (instance.isPlaying) {
            // Currently playing, pause it
            this.pauseTTS(id);
            return 'paused';
        } else {
            // Currently paused, resume it
            this.resumeTTS(id);
            return 'playing';
        }
    }

    /**
     * Get TTS state for a specific ID
     * @param {string} id - TTS instance identifier
     * @returns {Object} State information
     */
    getTTSState(id) {
        const instance = this.activeAudio.get(id);
        if (!instance) {
            return { exists: false, isPlaying: false, duration: 0, currentTime: 0 };
        }

        return {
            exists: true,
            isPlaying: instance.isPlaying,
            duration: instance.audio.duration || 0,
            currentTime: instance.audio.currentTime || 0
        };
    }

    /**
     * Pause all active TTS instances
     */
    pauseAllTTS() {
        this.activeAudio.forEach((instance, id) => {
            if (instance.isPlaying) {
                this.pauseTTS(id);
            }
        });
        console.log('⏸️ All TTS instances paused');
    }

    /**
     * Stop all active TTS instances
     */
    stopAllTTS() {
        const ids = Array.from(this.activeAudio.keys());
        ids.forEach(id => this.stopTTS(id));
        console.log('⏹️ All TTS instances stopped');
    }

    /**
     * Clean up audio resources for a specific ID
     * @param {string} id - TTS instance identifier
     */
    cleanupAudio(id) {
        const instance = this.activeAudio.get(id);
        if (instance) {
            // Revoke object URL to free memory
            if (instance.url) {
                URL.revokeObjectURL(instance.url);
                this.audioUrls.delete(instance.url);
            }
            // Remove from active instances
            this.activeAudio.delete(id);
            console.log('🧹 TTS audio cleaned up for:', id);
        }
    }

    /**
     * Clean up all audio resources
     */
    cleanup() {
        console.log('🧹 Cleaning up all TTS resources...');
        
        // Stop all audio
        this.stopAllTTS();
        
        // Revoke any remaining URLs
        this.audioUrls.forEach(url => {
            URL.revokeObjectURL(url);
        });
        
        // Clear collections
        this.activeAudio.clear();
        this.audioUrls.clear();
        
        console.log('✅ TTS cleanup complete');
    }

    /**
     * Auto-play TTS for assistant messages
     * @param {string} id - Message ID
     * @param {string} text - Text to speak
     * @param {Object} options - TTS options
     * @returns {Promise<void>}
     */
    async autoPlayTTS(id, text, options = {}) {
        const callbacks = {
            onPlay: () => console.log(`🔊 Auto-playing TTS for ${id}`),
            onEnd: () => console.log(`✅ Auto-play TTS completed for ${id}`),
            onError: (error) => console.error(`❌ Auto-play TTS error for ${id}:`, error)
        };

        await this.playTTS(id, text, options, callbacks.onPlay, callbacks.onEnd, callbacks.onError);
    }

    /**
     * Get list of all active TTS instances
     * @returns {Array<{id: string, isPlaying: boolean, duration: number, currentTime: number}>}
     */
    getActiveTTSList() {
        const activeList = [];
        this.activeAudio.forEach((instance, id) => {
            activeList.push({
                id: id,
                isPlaying: instance.isPlaying,
                duration: instance.audio.duration || 0,
                currentTime: instance.audio.currentTime || 0
            });
        });
        return activeList;
    }

    /**
     * Set volume for a specific TTS instance
     * @param {string} id - TTS instance identifier
     * @param {number} volume - Volume level (0.0 to 1.0)
     */
    setVolume(id, volume) {
        const instance = this.activeAudio.get(id);
        if (instance && instance.audio) {
            instance.audio.volume = Math.max(0, Math.min(1, volume));
            console.log(`🔊 Volume set to ${volume} for TTS:`, id);
        }
    }

    /**
     * Set volume for all active TTS instances
     * @param {number} volume - Volume level (0.0 to 1.0)
     */
    setVolumeAll(volume) {
        this.activeAudio.forEach((instance, id) => {
            if (instance.audio) {
                instance.audio.volume = Math.max(0, Math.min(1, volume));
            }
        });
        console.log(`🔊 Volume set to ${volume} for all TTS instances`);
    }
}

export default TTSService;

