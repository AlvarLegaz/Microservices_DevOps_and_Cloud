// Inicializar tareas en localStorage si no existen

    const initialTasks = [
      {
        "id": "1",
        "title": "Configurar red 5G con microcontrolador",
        "description": "Configurar una red 5G utilizando un microcontrolador AVR-IoT Cellular Mini Development Board",
        "doing": false,
        "done": false,
        "createdAt": "2024-08-26T12:00:00Z",
        "updatedAt": "2024-08-26T12:00:00Z"
      },
      {
        "id": "2",
        "title": "Desarrollar sensor IoT",
        "description": "Desarrollar un sensor IoT que envíe datos a través de una red 5G",
        "doing": true,
        "done": false,
        "createdAt": "2024-08-25T09:30:00Z",
        "updatedAt": "2024-08-26T13:00:00Z"
      },
      {
        "id": "3",
        "title": "Implementar seguridad en 5G",
        "description": "Implementar medidas de seguridad en dispositivos conectados a redes 5G utilizando microcontroladores",
        "doing": false,
        "done": true,
        "createdAt": "2024-08-20T08:00:00Z",
        "updatedAt": "2024-08-25T17:00:00Z"
      },
      {
        "id": "4",
        "title": "Optimizar consumo de energía",
        "description": "Optimizar el consumo de energía de dispositivos IoT conectados a redes 5G",
        "doing": true,
        "done": false,
        "createdAt": "2024-08-24T10:00:00Z",
        "updatedAt": "2024-08-26T14:00:00Z"
      }
    ];
    localStorage.setItem('tasks', JSON.stringify(initialTasks));

  
  // Leer tareas
  function readTasks() {
    return JSON.parse(localStorage.getItem('tasks'));
  }
  
  // Crear una nueva tarea
  function createTask(newTask) {
    const tasks = readTasks();
    tasks.push(newTask);
    localStorage.setItem('tasks', JSON.stringify(tasks));
    return tasks;
  }
  
  // Obtener una tarea por ID
  function getTaskById(taskId) {
    const tasks = readTasks();
    return tasks.find(task => task.id === taskId);
  }

  // Actualizar una tarea existente
  function updateTask(title, updatedTask) {
    const tasks = readTasks();
    const index = tasks.findIndex(task => task.title === title);
    if (index !== -1) {
      tasks[index] = { ...tasks[index], ...updatedTask, updatedAt: new Date().toISOString() };
      localStorage.setItem('tasks', JSON.stringify(tasks));
    }
    return tasks;
  }
  
  // Eliminar una tarea
  function deleteTask(title) {
    const tasks = readTasks();
    const index = tasks.findIndex(task => task.title === title);
    if (index !== -1) {
      tasks.splice(index, 1);
      localStorage.setItem('tasks', JSON.stringify(tasks));
    }
    return tasks;
  }
  