// src/main.tsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import App from './App';
import CompareInputPage from './components/CompareInputPage';
import './index.css';

console.log(`VITE_API_BASE_URL: ${import.meta.env.VITE_API_BASE_URL}`); // 環境変数をブラウザのコンソールに出力

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/compareinputpage" element={<CompareInputPage />} />
      </Routes>
    </Router>
  </React.StrictMode>,
);
