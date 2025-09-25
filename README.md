# Smart EV Camper - AI Voice Assistant

An intelligent voice assistant system for the Smart EV Camper project. This application features wake word detection, voice activity detection, AI-powered responses, and text-to-speech capabilities, all integrated into a modern web interface.

## 🚀 Features

- **Custom Wake Word**: Listens for "Hey Compass" using Picovoice Porcupine
- **Voice Activity Detection**: Automatically detects when you start and stop speaking
- **AI Assistant Integration**: Powered by advanced language models for intelligent responses
- **Text-to-Speech**: Natural voice responses using high-quality TTS models
- **Streaming Responses**: Real-time streaming of AI responses
- **Modern UI**: Beautiful, responsive interface with visual feedback
- **Resource Management**: Intelligent cleanup and resource management
- **Conversation History**: Maintains conversation context
- **Cross-platform**: Works on desktop and mobile browsers

## 📁 Project Structure

```
SMART_EV_CAMPER/
├── public/
│   ├── porcupine_params.pv      # Porcupine model file
│   └── Hey-Compass_en_wasm_v3_0_0.ppn  # Custom wake word model
├── src/
│   ├── services/
│   │   ├── PorcupineService.js  # Wake word detection service
│   │   ├── VADService.js        # Voice Activity Detection service
│   │   ├── AssistantService.js  # AI assistant API integration
│   │   └── TTSService.js        # Text-to-Speech service
│   ├── main.js                  # Main application logic
│   └── style.css               # Application styles
├── index.html                   # Main HTML file
├── wake-word-demo.html         # Demo page
├── vite.config.js              # Vite configuration
├── vercel.json                 # Vercel deployment config
└── package.json                # Dependencies and scripts
```

## 🛠️ Setup & Installation

### Prerequisites

- Node.js 16+
- Modern web browser with microphone support
- Internet connection (for AI assistant and TTS services)

### Dependencies

The application uses the following key dependencies:

```json
{
  "@picovoice/porcupine-web": "^3.0.3",
  "@picovoice/web-voice-processor": "^4.0.9",
  "@ricky0123/vad-web": "^0.0.22",
  "onnxruntime-web": "^1.14.0",
  "lucide": "latest"
}
```

### Running the Application

1. **Install dependencies:**
   ```bash
   pnpm install
   ```

2. **Start the development server:**
   ```bash
   pnpm dev
   ```

3. **Open your browser:**
   Navigate to `http://localhost:3000`

4. **Grant permissions:**
   - Allow microphone access when prompted
   - The app will automatically initialize all services

5. **Start the voice assistant:**
   - Click the microphone button to start listening
   - Say "Hey Compass" to activate the assistant
   - Speak your question or request
   - The assistant will respond with both text and speech

## 🔧 Configuration

### Model Files

The application uses two model files located in the `/public` directory:

- **`porcupine_params.pv`**: Main Porcupine model file
- **`Hey-Compass_en_wasm_v3_0_0.ppn`**: Custom wake word model for "Hey Compass"

### API Configuration

The application is pre-configured with hardcoded access keys and API endpoints. To modify:

1. **Assistant API**: Edit `src/services/AssistantService.js`
2. **TTS API**: Edit `src/services/TTSService.js`
3. **Wake Word Model**: Replace files in `/public` directory
4. **Voice Settings**: Modify TTS voice and model in `src/main.js`

## 🎯 Usage

### Voice Assistant Workflow

1. **Activation**: Click the microphone button to start listening for "Hey Compass"
2. **Wake Word**: Say "Hey Compass" clearly to activate the assistant
3. **Voice Input**: Speak your question or request naturally
4. **Processing**: The assistant processes your audio and generates a response
5. **Response**: Receive both text and audio responses
6. **Continuous**: The assistant remains active for follow-up questions

### Visual States

- **Blue Button**: Listening for wake word
- **Green Button**: Wake word detected, ready for speech
- **Red Button**: Recording your speech
- **Loading**: Processing your request

### Conversation Features

- **Streaming Responses**: See responses appear in real-time
- **Audio Playback**: Listen to natural voice responses
- **Conversation History**: View previous interactions
- **Auto-cleanup**: Resources are automatically managed

## 🔊 Audio Requirements

- **Microphone Access**: Required for wake word detection and voice input
- **Supported Browsers**: Chrome, Firefox, Safari, Edge (latest versions)
- **Audio Quality**: Clear speech in a quiet environment works best
- **Wake Word**: Say "Hey Compass" clearly and at normal speaking volume
- **Voice Input**: Speak naturally after wake word detection
- **Network**: Stable internet connection for AI and TTS services

## 🏗️ Architecture

### Service Layer

The application is built with a modular service architecture:

#### PorcupineService
- **Wake Word Detection**: Uses Picovoice Porcupine for "Hey Compass" detection
- **Microphone Management**: Handles audio permissions and stream management
- **Resource Cleanup**: Proper initialization and cleanup of Porcupine resources

#### VADService
- **Voice Activity Detection**: Automatically detects speech start/end using @ricky0123/vad-web
- **Audio Processing**: Converts Float32Array audio to base64 WAV format
- **Real-time Detection**: Provides callbacks for speech events

#### AssistantService
- **AI Integration**: Communicates with the iResearcher API for intelligent responses
- **Streaming Support**: Handles real-time streaming of AI responses
- **Audio Processing**: Sends audio data for transcription and processing
- **Conversation Management**: Maintains conversation context and history

#### TTSService
- **Text-to-Speech**: Converts AI responses to natural speech
- **Audio Management**: Handles multiple TTS instances and playback control
- **Resource Management**: Manages audio URLs and cleanup
- **Voice Configuration**: Supports different voices and models

### Main Application (WakeWordApp)

The main application orchestrates all services:

- **Service Coordination**: Manages the interaction between all services
- **State Management**: Tracks listening, processing, and conversation states
- **UI Updates**: Provides real-time visual feedback and status updates
- **Resource Management**: Ensures proper cleanup and resource management
- **Error Handling**: Comprehensive error handling across all services

## 🚀 Production Build

To build for production:

```bash
pnpm build
```

To preview the production build:

```bash
pnpm preview
```

## 🔒 Security & Privacy

- **Local Processing**: Wake word detection and VAD happen locally in the browser
- **API Communication**: Audio data is sent to external APIs for processing
- **No Local Storage**: Audio data is not stored locally
- **Microphone Access**: Used only for wake word detection and voice input
- **Conversation Data**: Conversation history is maintained in memory only
- **Resource Cleanup**: All audio resources are properly cleaned up after use

## 🛠️ Development

### Hot Reload

The application supports hot reload during development. Changes to source files will automatically refresh the browser.

### Debugging

- **Console Logs**: Check browser console for detailed service logs
- **Service Status**: Monitor service states and transitions
- **Network Tab**: Check API requests and responses
- **Audio Debugging**: Monitor audio processing and TTS playback

### Development Features

- **Verbose Logging**: Comprehensive logging across all services
- **Error Handling**: Detailed error messages and recovery
- **State Management**: Clear state transitions and debugging
- **Resource Monitoring**: Track resource usage and cleanup

## 📝 Customization

### Custom Wake Words

To use different wake words:

1. Create custom models at [Picovoice Console](https://console.picovoice.ai/)
2. Download the `.ppn` file
3. Replace the model file in `/public`
4. Update the `publicPath` and `label` in `PorcupineService.js`

### API Configuration

- **Assistant API**: Modify `src/services/AssistantService.js` for different AI models
- **TTS API**: Update `src/services/TTSService.js` for different voice services
- **Voice Settings**: Change voice and model in `src/main.js`

### UI Customization

- **Styling**: Modify `src/style.css` for visual changes
- **Layout**: Update `index.html` for structure changes
- **Behavior**: Customize interactions in `src/main.js`
- **Responses**: Adjust conversation display and formatting

### Service Configuration

- **VAD Settings**: Adjust sensitivity in `src/services/VADService.js`
- **TTS Options**: Configure voice, speed, and quality settings
- **Assistant Behavior**: Modify conversation handling and responses

## 🤝 Contributing

This is part of the Smart EV Camper project. Contributions and improvements are welcome!

## 📄 License

ISC License - See package.json for details

## 🚀 Deployment

The application is configured for deployment on Vercel:

- **Configuration**: `vercel.json` contains deployment settings
- **Build**: Uses Vite for optimized production builds
- **Static Assets**: All model files and resources are served from `/public`
- **Environment**: No environment variables required (all configs are hardcoded)

## 📊 Performance

- **Wake Word Detection**: ~50ms response time
- **Voice Processing**: Real-time audio processing
- **TTS Generation**: ~2-5 seconds depending on text length
- **Memory Usage**: Optimized resource management with automatic cleanup
- **Network**: Efficient API calls with streaming support

---

**Wake Word**: "Hey Compass" 🧭  
**AI Assistant**: Powered by advanced language models 🤖  
**Status**: Ready to assist! 🎤✨