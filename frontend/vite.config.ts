import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig(({ mode }) => {
  // Load environment variables based on the current mode ('development', 'production', etc.)
  const env = loadEnv(mode, process.cwd(), '')

  return {
    plugins: [react()],
    build: {
      outDir: 'dist' // この行が出力ディレクトリを指定しています
    },
    server: {
      port: 5173, // ローカルサーバーのポート番号を明示的に指定
      proxy: { // 環境に応じてプロキシ設定を変更
        '/api': {
          target: env.VITE_API_BASE_URL,
          changeOrigin: true, // rewriteオプションを削除
        },
      },
    },
  }
})
