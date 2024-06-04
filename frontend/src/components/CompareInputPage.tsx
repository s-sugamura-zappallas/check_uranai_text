// src/components/CompareInputPage.tsx
import React, { useState } from 'react';
import Sidebar from './Sidebar';

interface CompareResult {
    index_input: number;
    sub_title_input: string;
    check_order: string;
    check_text: boolean;
}

const CompareInputPage: React.FC = () => {
    const [inputHtml, setInputHtml] = useState('');
    const [resultHtml, setResultHtml] = useState('');
    const [company, setCompany] = useState('rsa');
    const [compareResult, setCompareResult] = useState<CompareResult[]>([]);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        try {
            const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;
            const response = await fetch(`${apiBaseUrl}/api/compare/inputpage`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: JSON.stringify({
                    company,
                    input_html: inputHtml,
                    result_html: resultHtml,
                }),
            });
            const data = await response.json();
            setCompareResult(data);
        } catch (error) {
            console.error('Error comparing input pages:', error);
        }
    };

    return (
        <div className="flex min-h-screen">
            <Sidebar />
            <div className="flex-grow p-8">
                <h1 className="text-3xl font-bold mb-6">Input Page Comparison</h1>
                <form onSubmit={handleSubmit} className="mb-8">
                    <div className="mb-4">
                        <label htmlFor="company" className="block mb-2 font-bold">Company:</label>
                        <select
                            id="company"
                            value={company}
                            onChange={(e) => setCompany(e.target.value)}
                            className="w-full p-2 border border-gray-300 rounded"
                        >
                            <option value="rsa">rsa</option>

                        </select>
                    </div>
                    <div className="mb-4">
                        <label htmlFor="inputHtml" className="block mb-2 font-bold">Input HTML:</label>
                        <textarea
                            id="inputHtml"
                            value={inputHtml}
                            onChange={(e) => setInputHtml(e.target.value)}
                            className="w-full p-2 border border-gray-300 rounded"
                            rows={5}
                        ></textarea>
                    </div>
                    <div className="mb-4">
                        <label htmlFor="resultHtml" className="block mb-2 font-bold">Result HTML:</label>
                        <textarea
                            id="resultHtml"
                            value={resultHtml}
                            onChange={(e) => setResultHtml(e.target.value)}
                            className="w-full p-2 border border-gray-300 rounded"
                            rows={5}
                        ></textarea>
                    </div>
                    <button
                        type="submit"
                        className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded"
                    >
                        Compare
                    </button>
                </form>
                {compareResult.length > 0 && (
                    <table className="w-full bg-white shadow-md rounded">
                        <thead>
                            <tr>
                                <th className="px-4 py-2">Sub Title Input</th>
                                <th className="px-4 py-2">Check Order</th>
                                <th className="px-4 py-2">Check Text</th>
                            </tr>
                        </thead>
                        <tbody>
                            {compareResult.map((item, index) => (
                                <tr
                                    key={index}
                                    className={`${item.check_order === 'Item Missing or Created with Image' ||
                                        item.check_text === false
                                        ? 'bg-red-200'
                                        : item.check_order === 'Next Item Missing or Created with Image'
                                            ? 'bg-yellow-200'
                                            : 'bg-green-200'
                                        }`}
                                >
                                    <td className="border px-4 py-2">{item.sub_title_input}</td>
                                    <td className="border px-4 py-2">{item.check_order}</td>
                                    <td className="border px-4 py-2">{item.check_text ? 'True' : 'False'}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                )}
            </div>
        </div>
    );
};

export default CompareInputPage;