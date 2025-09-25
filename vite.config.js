import { defineConfig } from 'vite';

export default defineConfig({
  // Configure server for development
  server: {
    host: true,
    port: 3000,
    // Enable HTTPS if needed for microphone access
    // https: true,
    headers: {
      // Enable Cross-Origin Embedder Policy for SharedArrayBuffer support
      'Cross-Origin-Embedder-Policy': 'require-corp',
      'Cross-Origin-Opener-Policy': 'same-origin',
    },
  },

  // Build configuration
  build: {
    // Ensure proper asset handling
    assetsDir: 'assets',
    rollupOptions: {
      // Ensure model files are copied to build output
      input: {
        main: './index.html',
      },
    },
  },

  // Public directory configuration
  publicDir: 'public',

  // Optimize dependencies
  optimizeDeps: {
    include: [
      '@picovoice/porcupine-web',
      '@picovoice/web-voice-processor'
    ],
  },

  // Configure asset handling
  assetsInclude: ['**/*.pv', '**/*.ppn'],

  // Development server configuration for model files
  define: {
    // Enable development mode features
    __DEV__: JSON.stringify(process.env.NODE_ENV === 'development'),
  },

  // Preview configuration (for production preview)
  preview: {
    host: true,
    port: 4173,
    headers: {
      'Cross-Origin-Embedder-Policy': 'require-corp',
      'Cross-Origin-Opener-Policy': 'same-origin',
    },
  },
});

