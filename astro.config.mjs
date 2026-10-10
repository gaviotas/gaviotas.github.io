import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://gaviotas.github.io',
  output: 'static',
  server: { host: '127.0.0.1', port: 4000 },
  devToolbar: { enabled: false },
});
