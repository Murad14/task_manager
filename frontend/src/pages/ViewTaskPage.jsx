import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ViewTaskPage = () => {
    const [tasks, setTasks] = useState([]);

    useEffect(() => {
        const fetchTasks = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/todo/tasks/', {
                    headers: {
                        Authorization: 'Bearer YOUR_ACCESS_TOKEN',
                    },
                });
                setTasks(response.data);
            } catch (error) {
                console.error('Error fetching tasks:', error);
            }
        };

        fetchTasks();
    }, []);

    return (
        <div>
            <h1>View Task Page</h1>
            <ul>
                {tasks.map((task) => (
                    <li key={task.id}>{task.title}</li>
                ))}
            </ul>
        </div>
    );
};

export default ViewTaskPage;

