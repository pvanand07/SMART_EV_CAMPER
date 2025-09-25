I'll create an architecture diagram in markdown showing the complete flow of your simplified voice assistant application:

```markdown
# Voice Assistant Architecture Flow

## System Components

```mermaid
graph TB
    UI[🎤 Mic Button UI] --> App[VoiceAssistantApp]
    App --> VAD[VADService]
    App --> AST[AssistantService]
    App --> TTS[TTSService]
    App --> DOM[DOM Elements]
```

## Main Application Flow

```mermaid
sequenceDiagram
    participant User
    participant UI as 🎤 Mic Button
    participant App as VoiceAssistantApp
    participant VAD as VADService
    participant AST as AssistantService
    participant TTS as TTSService

    Note over User,TTS: Initial State: Ready to Listen
    User->>UI: Click Mic Button
    UI->>App: toggleListening()
    App->>App: stopAllActivities()
    Note over App: Stop any ongoing TTS/VAD/Processing
    
    alt Not Listening (Start Flow)
        App->>VAD: start()
        App->>UI: Update to Listening State (Blue)
        Note over App: isListening = true
        
        alt Speech Detected
            VAD->>App: onVADSpeechStart()
            App->>UI: Update to Recording State (Red)
            Note over User: User speaks...
            VAD->>App: onVADSpeechEnd(audioData)
            App->>VAD: stop()
            App->>UI: Update to Processing State
            Note over App: isProcessingAudio = true
            
            App->>AST: sendAudioQuery(audioBase64)
            AST->>App: onStreamingStart()
            App->>DOM: Create Assistant Message
            
            loop Streaming Response
                AST->>App: onStreamingChunk(chunk)
                App->>DOM: Update Message Content
            end
            
            AST->>App: onStreamingComplete(response)
            App->>DOM: Finalize Message
            App->>TTS: autoPlayTTS(response)
            Note over App: isProcessingAudio = false
            TTS->>App: TTS Complete
            App->>App: resetToDefaultState()
            App->>UI: Return to Ready State (Gray)
            
        else Timeout (10s no speech)
            App->>VAD: stop()
            App->>App: resetToDefaultState()
            App->>UI: Return to Ready State
        end
        
    else Currently Listening (Stop Flow)
        App->>VAD: stop()
        App->>App: resetToDefaultState()
        App->>UI: Return to Ready State
    end
```

## State Management

```mermaid
stateDiagram-v2
    [*] --> Ready: App Initialize
    
    Ready --> Listening: Click Mic (Start)
    Listening --> Recording: Speech Detected
    Listening --> Ready: Click Mic (Stop) / Timeout
    
    Recording --> Processing: Speech Ended
    Processing --> PlayingTTS: Assistant Response
    PlayingTTS --> Ready: TTS Complete
    
    Listening --> Ready: stopAllActivities()
    Recording --> Ready: stopAllActivities()
    Processing --> Ready: stopAllActivities()
    PlayingTTS --> Ready: stopAllActivities()
    
    note right of Ready
        - Gray mic button
        - "Click microphone to start"
        - isListening = false
        - isProcessingAudio = false
    end note
    
    note right of Listening
        - Blue mic button
        - "Listening for speech..."
        - isListening = true
        - 10s timeout active
    end note
    
    note right of Recording
        - Red mic button (recording animation)
        - "Listening to your speech..."
        - Speech being captured
    end note
    
    note right of Processing
        - Processing state
        - "Processing your speech..."
        - isProcessingAudio = true
        - Audio → Base64 → Assistant
    end note
    
    note right of PlayingTTS
        - Playing response audio
        - "Playing response audio..."
        - Text response visible in UI
    end note
```

## Key Features

### 🎯 **Click-to-Interrupt**
- Mic button press **always** stops all activities immediately
- Works in any state: Listening, Recording, Processing, or TTS playback
- Provides instant user control

### 🔄 **Conversation Persistence**
- Same conversation ID maintained throughout session
- No conversation reset on mic clicks
- Context preserved across interactions

### ⏱️ **Timeout Handling**
- 10-second timeout when listening for speech
- Auto-return to ready state if no speech detected
- Prevents hanging in listening mode

### 🎵 **Audio Flow**
- VAD captures speech → Base64 WAV conversion
- Assistant streaming response with real-time UI updates
- Auto-play TTS with voice: 'af_bella', model: 'hexgrad/Kokoro-82M'

## Service Responsibilities

| Service | Responsibility |
|---------|----------------|
| **VoiceAssistantApp** | Main orchestrator, state management, UI updates |
| **VADService** | Voice Activity Detection, speech capture |
| **AssistantService** | AI conversation, streaming responses |
| **TTSService** | Text-to-speech playback, audio management |

## Error Handling

```mermaid
graph TD
    Error[Any Error Occurs] --> Stop[stopAllActivities()]
    Stop --> Reset[resetToDefaultState()]
    Reset --> UI[Update UI to Ready State]
    UI --> Log[Log Error to Console]
```

All errors result in a clean return to the ready state, ensuring the app never gets stuck in an error condition.
```

This architecture shows your simplified voice assistant with:
- **Single-click activation/deactivation**
- **Immediate interruption capability**
- **Persistent conversation context**
- **Clean state management**
- **Robust error handling**

The flow is much cleaner than the original wake-word system, giving users direct control while maintaining conversation continuity.