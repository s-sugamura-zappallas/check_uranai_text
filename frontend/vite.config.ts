import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist' // この行が出力ディレクトリを指定しています
  },
  server: {
    port: 5173, // ローカルサーバーのポート番号を明示的に指定
    proxy: {
      // ローカル開発用のプロキシ設定
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        //rewrite: (path) => path.replace(/^\/api/, ''),
      },
      // デプロイ用のプロキシ設定
      '/api-prod': {
        target: 'https://83g13mb9p1.execute-api.ap-northeast-1.amazonaws.com/prod',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api-prod/, '/api'),
      },
    },
  },
})
