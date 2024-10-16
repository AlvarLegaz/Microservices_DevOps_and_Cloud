/**
 * Fetches the list of tasks for a given user.
 * @param {string} base_url - The base URL of the API.
 * @param {string} user - The username.
 * @param {string} token_jwt - The JWT token for authorization.
 */

async function getTasksList(base_url, user, api_key, token_jwt) {
	console.log('api key:', api_key);
	console.log('token:', token_jwt);
    try {
	const response = await fetch(`${base_url}/todo/${user}`, {
	    method: 'GET',
	    headers: {
			'X-ApiKey': api_key,
	        'Authorization': token_jwt,
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
	return data;

    } catch (error) {
	console.error('Error al cargar las tareas:', error);
    }
}


async function createTask(task, base_url, user, api_key, token_jwt) {
    try {
	const response = await fetch(`${base_url}/todo/${user}`, {
	    method: 'POST',
	    headers: {
			'X-ApiKey': api_key,
	        'Authorization': `Bearer ${token_jwt}`,
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
    	console.error('Tarea:', task);
	console.error('Error al cargar las tareas:', error);
    }
}

async function getTaskById(id, base_url, user, api_key, token_jwt) {
    try {
	const response = await fetch(`${base_url}/todo/${user}/${id}`, {
	    method: 'GET',
	    headers: {
			'X-ApiKey': api_key,
	        'Authorization': `Bearer ${token_jwt}`,
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


async function deleteTaskById(id, base_url, user,  api_key, token_jwt) {
    try {
	const response = await fetch(`${base_url}/todo/${user}/${id}`, {
	    method: 'DELETE',
	    headers: {
			'X-ApiKey': api_key,
	        'Authorization': `Bearer ${token_jwt}`,
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


async function updateTaskById(id, task, base_url, user,  api_key, token_jwt) {
    try {
	const response = await fetch(`${base_url}/todo/${user}/${id}`, {
	    method: 'PUT',
	    headers: {
			'X-ApiKey': api_key,
	        'Authorization': `Bearer ${token_jwt}`,
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
