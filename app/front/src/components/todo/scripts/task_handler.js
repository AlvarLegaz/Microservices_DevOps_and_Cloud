const tasks = [
    {
        "title": "Configurar red 5G con microcontrolador",
        "description": "Configurar una red 5G utilizando un microcontrolador AVR-IoT Cellular Mini Development Board",
        "doing": false,
        "done": false,
        "createdAt": "2024-08-26T12:00:00Z",
        "updatedAt": "2024-08-26T12:00:00Z"
    },
    {
        "title": "Desarrollar sensor IoT",
        "description": "Desarrollar un sensor IoT que envíe datos a través de una red 5G",
        "doing": true,
        "done": false,
        "createdAt": "2024-08-25T09:30:00Z",
        "updatedAt": "2024-08-26T13:00:00Z"
    },
    {
        "title": "Implementar seguridad en 5G",
        "description": "Implementar medidas de seguridad en dispositivos conectados a redes 5G utilizando microcontroladores",
        "doing": false,
        "done": true,
        "createdAt": "2024-08-20T08:00:00Z",
        "updatedAt": "2024-08-25T17:00:00Z"
    },
    {
        "title": "Optimizar consumo de energía",
        "description": "Optimizar el consumo de energía de dispositivos IoT conectados a redes 5G",
        "doing": true,
        "done": false,
        "createdAt": "2024-08-24T10:00:00Z",
        "updatedAt": "2024-08-26T14:00:00Z"
    }
];

async function fetchTasks() {
    try {
        const response = await new Promise((resolve) => {
            setTimeout(() => resolve(tasks), 1000);
        });

        displayTasks(response);
    } catch (error) {
        console.error('Error al cargar las tareas:', error);
    }
}

function displayTasks(tasks) {
    const todoContainer = document.getElementById('toDo');
    const doingContainer = document.getElementById('doing');
    const doneContainer = document.getElementById('done');

    todoContainer.innerHTML = '';
    doingContainer.innerHTML = '';
    doneContainer.innerHTML = '';

    tasks.forEach(task => {
        const taskCard = document.createElement('div');
        taskCard.classList.add('task');
        if (task.doing) {
            taskCard.classList.add('doing');
            doingContainer.appendChild(taskCard);
        } else if (task.done) {
            taskCard.classList.add('done');
            doneContainer.appendChild(taskCard);
        } else {
            todoContainer.appendChild(taskCard);
        }
        taskCard.innerHTML = `
            <div class="card" onclick="toggleDescription(this)">
                <h4>${task.title}</h4>
                <div class="description" style="display: none;">
                    <p>${task.description}</p>
                </div>    
                <div class="doing" style="display: none;">    
                    <p><strong>Doing:</strong> ${task.doing}</p>
                </div>    
                <div class="done" style="display: none;">     
                    <p><strong>Done:</strong> ${task.done}</p>
                </div>    
                <div class="created" style="display: none;"> 
                    <p><strong>Created At:</strong> ${task.createdAt}</p>
                </div>    
                <div class="updated" style="display: none;"> 
                    <p><strong>Updated At:</strong> ${task.updatedAt}</p>
                </div> 
                <div class="buttons" style="display: none;">   
                    <br>
                    <button class="btn_edit_task">Edit</button>
                    <button class="btn_rmv_task">Delete</button>
                    <button class="btn_close_task">Close</button>
                </div>    
            </div>
        `;
    });
}

fetchTasks();