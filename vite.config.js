import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { VitePWA } from 'vite-plugin-pwa';

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    react(),
    VitePWA({
      registerType: 'autoUpdate',
      devOptions: {
        enabled: true
      },
      manifest: {
        name: 'Disaster Response Command',
        short_name: 'DRC',
        description: 'Advanced Disaster Response and Reporting Platform',
        theme_color: '#0b132b',
        background_color: '#0b132b',
        display: 'standalone',
        icons: [
          {
            src: 'https://cdn-icons-png.flaticon.com/512/12133/12133041.png', // Temporary generic icon
            sizes: '192x192',
            type: 'image/png'
          },
          {
            src: 'https://cdn-icons-png.flaticon.com/512/12133/12133041.png',
            sizes: '512x512',
            type: 'image/png'
          }
        ]
      }
    })
  ],
});
