import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

const config = {
  kit: {
    adapter: adapter({
			fallback: '200.html' // may differ from host to host
		})
  },
  preprocess: vitePreprocess()
};

export default config;
