import React, { useState, useEffect } from 'react';

export default function HomePage() {
    const [tasks, setTasks] = useState([]);
    const [taskTitle, setTaskTitle] = useState('');
    const [taskDescription, setTaskDescription] = useState('');
    const [taskDueDate, setTaskDueDate] = useState('');
    const [taskPriority, setTaskPriority] = useState('Medium');
    const [taskIsComplete, setTaskIsComplete] = useState(false);
    const [taskImage, setTaskImage] = useState(null);

    const fetchTasks = async () => {
        try {
            const token = localStorage.getItem('token');

            if (!token) {
                console.error('Token not found in localStorage');
                return;
            }

            const response = await fetch('http://127.0.0.1:8000/api/todo/tasks/', {
                headers: {
                    'Authorization': `Bearer ${token}`,
                },
            });

            if (response.ok) {
                const data = await response.json();
                console.log('Fetched tasks:', data);
                setTasks(data);
                return data;  // Return the fetched data
            } else {
                console.error('Error fetching tasks:', response.statusText);
            }
        } catch (error) {
            console.error('Error fetching tasks:', error);
        }
    };

    useEffect(() => {
        fetchTasks();
    }, []);  // Empty dependency array to run the effect only once

    const handleCreateTask = async () => {
        try {
            const formData = new FormData();
            formData.append('title', taskTitle);
            formData.append('description', taskDescription);
            formData.append('due_date', taskDueDate);
            formData.append('priority', taskPriority);
            formData.append('is_complete', taskIsComplete);
            formData.append('image', taskImage);

            const response = await fetch('http://127.0.0.1:8000/api/todo/tasks/', {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('token')}`,
                },
                body: formData,
            });

            if (response.ok) {
                console.log('Task created successfully');
                // Fetch updated tasks and update the list
                const updatedTasks = await fetchTasks();
                setTasks(updatedTasks);
            } else {
                console.error('Error creating task:', response.statusText);
            }
        } catch (error) {
            console.error('Error creating task:', error);
        }
    };


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
                <h2 className="text-2xl font-semibold mb-4">Your Tasks</h2>
                <form>
                    <div className="mb-4">
                        <label htmlFor="taskTitle" className="block text-gray-700 text-sm font-bold mb-2">
                            Task Title
                        </label>
                        <input
                            type="text"
                            id="taskTitle"
                            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                            placeholder="Enter task title"
                            value={taskTitle}
                            onChange={(e) => setTaskTitle(e.target.value)}
                        />
                    </div>
                    <div className="mb-4">
                        <label htmlFor="taskDescription" className="block text-gray-700 text-sm font-bold mb-2">
                            Task Description
                        </label>
                        <textarea
                            id="taskDescription"
                            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                            placeholder="Enter task description"
                            value={taskDescription}
                            onChange={(e) => setTaskDescription(e.target.value)}
                        />
                    </div>
                    <div className="mb-4">
                        <label htmlFor="taskDueDate" className="block text-gray-700 text-sm font-bold mb-2">
                            Due Date
                        </label>
                        <input
                            type="date"
                            id="taskDueDate"
                            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                            value={taskDueDate}
                            onChange={(e) => setTaskDueDate(e.target.value)}
                        />
                    </div>
                    <div className="mb-4">
                        <label htmlFor="taskPriority" className="block text-gray-700 text-sm font-bold mb-2">
                            Priority
                        </label>
                        <select
                            id="taskPriority"
                            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                            value={taskPriority}
                            onChange={(e) => setTaskPriority(e.target.value)}
                        >
                            <option value="Low">Low</option>
                            <option value="Medium">Medium</option>
                            <option value="High">High</option>
                        </select>
                    </div>
                    <div className="mb-4">
                        <label htmlFor="taskIsComplete" className="block text-gray-700 text-sm font-bold mb-2">
                            Is Complete
                        </label>
                        <input
                            type="checkbox"
                            id="taskIsComplete"
                            className="form-checkbox h-5 w-5 text-blue-500"
                            checked={taskIsComplete}
                            onChange={() => setTaskIsComplete(!taskIsComplete)}
                        />
                    </div>
                    <div className="mb-4">
                        <label htmlFor="taskImage" className="block text-gray-700 text-sm font-bold mb-2">
                            Task Image
                        </label>
                        <input
                            type="file"
                            id="taskImage"
                            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                            accept="image/*"
                            onChange={(e) => setTaskImage(e.target.files[0])}
                        />
                    </div>

                    <button
                        type="button"
                        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                        onClick={handleCreateTask}
                    >
                        Create Task
                    </button>
                </form>

                <button
                    className="mt-4 bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                    onClick={() => console.log('Implement logic to view all tasks')}
                >
                    View All Tasks
                </button>
            </div>
        </div>
    );

}