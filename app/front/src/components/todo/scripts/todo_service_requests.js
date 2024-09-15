async function fetchTasks() {
    try {
        const response = await fetch('http://127.0.0.1:3001/todo/alvar', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            mode: 'cors'
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(JSON.stringify(errorData));
        }

        const data = await response.json();
        console.log('Get list data:', data);
        displayTasks(data);

    } catch (error) {
        console.error('Error al cargar las tareas:', error);
    }
}

async function getTaskById(id) {
    try {
        const response = await fetch(`http://127.0.0.1:3001/todo/alvar/${id}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            mode: 'cors'
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(JSON.stringify(errorData));
        }

        const task = await response.json();
        return task;

    } catch (error) {
        console.error('Error al cargar la tarea:', error);
        throw error;
    }
}