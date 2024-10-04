async function getTasksList() {
    try {
        const response = await fetch(`${base_url}/todo/${user}`, {
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

async function createTask(task) {
    try {
        const response = await fetch(`{base_url}/todo/${user}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            mode: 'cors',
            body: JSON.stringify(task)
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(JSON.stringify(errorData));
        }

        const data = await response.json();
        console.log('Updated task:', data);
    } 
    catch (error) {
        console.error('Error al cargar las tareas:', error);
    }
}

async function getTaskById(id) {
    try {
        const response = await fetch(`{base_url}/todo/${user}/${id}`, {
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

async function deleteTaskById(id) {
    try {
        const response = await fetch(`{base_url}/todo/${user}/${id}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            mode: 'cors'
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(JSON.stringify(errorData));
        }

        return response;

    } catch (error) {
        console.error('Error al cargar la tarea:', error);
        throw error;
    }
}

async function updateTaskById(id, task) {
    try {
        const response = await fetch(`{base_url}/todo/${user}/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            mode: 'cors',
            body: JSON.stringify(task)
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(JSON.stringify(errorData));
        }

        const data = await response.json();
        console.log('Updated task:', data);

    } catch (error) {
        console.error('Error al cargar las tareas:', error);
    }
}
