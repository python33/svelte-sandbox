import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
  hmr: {
      port: 5173,
      polling: true,
  },
  server: {
    proxy: {
      '/api': {
        target: 'https://history-tests.eu.ngrok.io',
        changeOrigin: true,
      },
    },
  }
});
