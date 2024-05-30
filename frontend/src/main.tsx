import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'

console.log(`VITE_API_BASE_URL: ${import.meta.env.VITE_API_BASE_URL}`); // 環境変数をブラウザのコンソールに出力

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
