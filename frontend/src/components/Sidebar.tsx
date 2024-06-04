// src/components/Sidebar.tsx
import React from 'react';
import { Link } from 'react-router-dom';

const Sidebar: React.FC = () => {
    return (
        <div className="bg-gray-800 text-white min-h-screen p-4 flex-shrink-0">
            <h2 className="text-2xl font-bold mb-4">Menu</h2>
            <ul className="space-y-2">
                <li>
                    <Link to="/" className="block py-2 px-4 hover:bg-gray-700 rounded">
                        Top Page
                    </Link>
                </li>
                <li>
                    <Link to="/compareinputpage" className="block py-2 px-4 hover:bg-gray-700 rounded">
                        Input Page
                    </Link>
                </li>
            </ul>
        </div>
    );
};

export default Sidebar;
