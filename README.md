# Smart EV Camper - Wake Word Detection

A wake word detection system using Picovoice Porcupine for the Smart EV Camper project. This application listens for the custom wake word "Hey Compass" and provides a modern web interface for interaction.

## 🚀 Features

- **Custom Wake Word**: Listens for "Hey Compass"
- **Real-time Detection**: Instant wake word recognition
- **Modern UI**: Beautiful, responsive interface
- **Activity Logging**: Real-time activity and detection logs
- **Permission Management**: Handles microphone permissions gracefully
- **Visual Feedback**: Alert notifications when wake word is detected

## 📁 Project Structure

```
SMART_EV_CAMPER/
├── public/
│   ├── porcupine_params.pv      # Porcupine model file
│   └── Hey-Compass_en_wasm_v3_0_0.ppn  # Custom wake word model
├── src/
│   ├── services/
│   │   └── PorcupineService.js  # Wake word detection service
│   ├── main.js                  # Main application logic
│   └── style.css               # Application styles
├── index.html                   # Main HTML file
├── vite.config.js              # Vite configuration
└── package.json                # Dependencies and scripts
```

## 🛠️ Setup & Installation

### Prerequisites

- Node.js 16+
- Picovoice Access Key ([Get one here](https://console.picovoice.ai/))
- Modern web browser with microphone support

### Dependencies Already Installed

The following dependencies are already installed:

```json
{
  "@picovoice/porcupine-web": "^3.0.3",
  "@picovoice/web-voice-processor": "^4.0.9"
}
```

### Running the Application

1. **Start the development server:**
   ```bash
   pnpm dev
   ```

2. **Open your browser:**
   Navigate to `http://localhost:3000`

3. **Configure the application:**
   - Enter your Picovoice Access Key
   - Grant microphone permission
   - Click "Start Listening"

4. **Test the wake word:**
   Say "Hey Compass" to trigger detection

## 🔧 Configuration

### Model Files

The application uses two model files located in the `/public` directory:

- **`porcupine_params.pv`**: Main Porcupine model file
- **`Hey-Compass_en_wasm_v3_0_0.ppn`**: Custom wake word model for "Hey Compass"

### Access Key

You need a Picovoice Access Key to use this application:

1. Sign up at [Picovoice Console](https://console.picovoice.ai/)
2. Create a new project
3. Copy your Access Key
4. Enter it in the application interface

## 🎯 Usage

### Starting Detection

1. Enter your Picovoice Access Key
2. Grant microphone permission when prompted
3. Click "Start Listening"
4. The status will show "🎤 Listening for 'Hey Compass'..."

### Wake Word Detection

- Say "Hey Compass" clearly
- The application will detect the wake word and show:
  - A visual alert popup
  - Log entry with timestamp
  - Console output

### Stopping Detection

- Click "Stop Listening" to stop wake word detection
- Resources will be properly released

## 🔊 Audio Requirements

- **Microphone Access**: Required for wake word detection
- **Supported Browsers**: Chrome, Firefox, Safari, Edge
- **Audio Quality**: Clear speech in a quiet environment works best
- **Wake Word**: Say "Hey Compass" clearly and at normal speaking volume

## 🏗️ Architecture

### PorcupineService Class

The `PorcupineService` class handles all wake word detection functionality:

- **Initialization**: Sets up Porcupine with custom models
- **Listening Control**: Start/stop detection
- **Resource Management**: Proper cleanup and resource release
- **Error Handling**: Comprehensive error management
- **Permission Handling**: Microphone permission management

### Main Application

The main application provides:

- **UI Management**: Controls and status updates
- **Event Handling**: User interactions and system events
- **Logging**: Activity and detection logging
- **Visual Feedback**: Alerts and status indicators

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

- **Access Key**: Keep your Picovoice Access Key secure
- **Local Processing**: All wake word detection happens locally
- **No Data Storage**: Audio is not stored or transmitted
- **Microphone Access**: Only used for wake word detection

## 🛠️ Development

### Hot Reload

The application supports hot reload during development. Changes to source files will automatically refresh the browser.

### Debugging

- Check browser console for detailed logs
- Use the activity log in the UI for real-time monitoring
- Enable verbose logging by modifying the PorcupineService class

## 📝 Customization

### Custom Wake Words

To use different wake words:

1. Create custom models at [Picovoice Console](https://console.picovoice.ai/)
2. Download the `.ppn` file
3. Replace the model file in `/public`
4. Update the `publicPath` and `label` in `PorcupineService.js`

### UI Customization

- Modify `src/style.css` for styling changes
- Update `index.html` for structure changes
- Customize alerts and notifications in `src/main.js`

## 🤝 Contributing

This is part of the Smart EV Camper project. Contributions and improvements are welcome!

## 📄 License

ISC License - See package.json for details

---

**Wake Word**: "Hey Compass" 🧭
**Status**: Ready to listen! 🎤