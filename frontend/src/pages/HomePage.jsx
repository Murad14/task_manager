import React from 'react';

export default function HomePage() {
    return (
        <div>
            <nav className="shadow-lg">
                <div className="px-4 mx-auto">
                    <div className="flex justify-between">
                        <div>
                            <a className="flex" href="/home">
                                <span className="font-semibold text-lg text-gray-500">Task Manager</span>
                            </a>
                        </div>
                        <div className="space-x-1">
                            <a className="py-4 px-2 text-gray-500 font-semibold" href="/profile">
                                Profile
                            </a>
                            <a className="py-4 px-2 text-gray-500 font-semibold" href="/logout">
                                Logout
                            </a>
                        </div>
                    </div>
                </div>
            </nav>


            <div className="p-4">

            </div>
        </div>
    );
}

