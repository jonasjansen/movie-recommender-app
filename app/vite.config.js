// app/vite.config.js
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import { createProxyMiddleware } from 'http-proxy-middleware';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: process.env.NODE_ENV === 'development'
      ? {
        proxy: {
          '/api': {
            target: 'http://localhost:5000',
            changeOrigin: true,
            rewrite: (path) => path.replace(/^\/api/, ''),
          },
        },
      }
      : undefined,
});
