import { useState, useRef } from 'react';
import './App.css';

interface ComparisonItem {
  menu_html: string;
  caption_html: string;
  price_html: number;
  is_same_set: boolean;
  diff_menu: number;
  diff_caption: number;
  diff_price: number;
}

type ComparisonResult = ComparisonItem[];

const companies = ['rsa', 'zap']; // 会社名の配列

function App() {
  const [selectedCompany, setSelectedCompany] = useState(companies[0]);
  const [html, setHtml] = useState('');
  const [csvFile, setCsvFile] = useState<File | null>(null);
  const [result, setResult] = useState<ComparisonResult | null>(null);
  const [error, setError] = useState<string | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleCompanyChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setSelectedCompany(event.target.value);
  };

  const handleHtmlChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
    setHtml(event.target.value);
  };

  const handleCsvChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files && event.target.files[0]) {
      setCsvFile(event.target.files[0]);
    }
  };

  const handleSubmit = async () => {
    if (!selectedCompany || !html || !csvFile) {
      setError("Please fill in all fields.");
      return;
    }
    setError(null);

    const formData = new FormData();
    formData.append('company', selectedCompany);
    formData.append('html', html);
    formData.append('csv', csvFile);

    try {
      const response = await fetch('/api/compare/toppage', {
        method: 'POST',
        body: formData,
      });
      if (!response.ok) {
        const errorData = await response.json();
        console.error('Error details:', errorData); // エラーの詳細をコンソールに出力
        setError("An error occurred while processing the request."); // ユーザーにわかりやすいメッセージを表示
        return;
      }
      const data = await response.json();
      setResult(data);
    } catch (error: unknown) {
      if (error instanceof Error) {
        setError(error.message);
      } else {
        setError("An unknown error occurred.");
      }
    }
  };

  const handleReset = () => {
    setSelectedCompany(companies[0]);
    setHtml('');
    setCsvFile(null);
    setResult(null);
    setError(null);
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  };

  return (
    <div className="App max-w-4xl mx-auto p-4">
      <h1 className="text-3xl font-bold mb-8">Top Page Comparison</h1>
      
      <div className="mb-4">
        <label htmlFor="company" className="block mb-2 font-bold">Company:</label>
        <select 
          id="company"
          value={selectedCompany ?? null}
          onChange={handleCompanyChange}
          className="w-full p-2 border border-gray-300 rounded"
        >
          <option value="">Select Company</option>
          {companies.map((company) => (
            <option key={company} value={company}>
              {company}
            </option>
          ))}
        </select>
      </div>
      
      <div className="mb-4">
        <label htmlFor="html" className="block mb-2 font-bold">HTML:</label>
        <textarea
          id="html"
          value={html}
          onChange={handleHtmlChange}
          className="w-full p-2 border border-gray-300 rounded"
          rows={6}
        />
      </div>
      
      <div className="mb-4">
        <label htmlFor="csv" className="block mb-2 font-bold">CSV File:</label>
        <input 
          type="file"
          id="csv"
          accept=".csv"
          onChange={handleCsvChange}
          className="w-full"
          ref={fileInputRef}
        />
      </div>
      
      <div className="flex space-x-4">
        <button 
          onClick={handleSubmit}
          className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded"
        >
          Compare
        </button>
        <button
          onClick={handleReset}
          className="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded"
        >
          Reset
        </button>
      </div>
      
      {error && <p className="mt-4 text-red-500">{error}</p>}
      
      {result && (
        <div className="mt-8">
          <h2 className="text-2xl font-bold mb-4">Comparison Result:</h2>
          
          <table className="w-full border-collapse">
            <thead>
              <tr>
                <th className="border p-2">menu_html</th>
                <th className="border p-2">caption_html</th>
                <th className="border p-2">price_html</th>
              </tr>
            </thead>
            <tbody>
              {result.map((item, index) => (
                <tr key={index}>
                  <td className={`border p-2 ${item.diff_menu === 0 ? 'bg-green-100' : 'bg-red-100'}`}>
                    <div className={item.diff_menu === 0 ? 'text-green-800' : 'text-red-800'}>
                      {item.menu_html}
                    </div>
                  </td>
                  <td className={`border p-2 ${item.diff_caption === 0 ? 'bg-green-100' : 'bg-red-100'}`}>
                    <div className={item.diff_caption === 0 ? 'text-green-800' : 'text-red-800'}>
                      {item.caption_html}  
                    </div>
                  </td>
                  <td className={`border p-2 ${item.diff_price === 0 ? 'bg-green-100' : 'bg-red-100'}`}>
                    <div className={item.diff_price === 0 ? 'text-green-800' : 'text-red-800'}>
                      {item.price_html}
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
          
        </div>
      )}
    </div>
  );
}

export default App;