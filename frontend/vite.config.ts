import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist' // この行が出力ディレクトリを指定しています
  },
  server: {
    proxy: {
      '/api': 'http://localhost:8000',
    },
  },
})
