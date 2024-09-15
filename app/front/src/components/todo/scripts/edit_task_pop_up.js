document.addEventListener('DOMContentLoaded', function() {
    // Crear el popup y añadirlo al body
    const edit_popup = document.createElement('div');
    edit_popup.id = 'edit_popup';
    edit_popup.className = 'popup';
    edit_popup.innerHTML = `
        <div class="popup-content">
            <span class="close-btn">&times;</span>
            <spam id="task_id">Task id</spam><br><br>
            <textarea class="input-style" id="title" name="title" rows="2"></textarea><br><br>
            <textarea class="input-style" id="description" name="edit" rows="4"></textarea><br><br>
            <textarea class="input-style" id="created" name="edit" rows="1"></textarea><br><br>
            <textarea class="input-style" id="updated" name="edit" rows="1"></textarea><br><br>
            <input type="submit" class="update-task-btn" value="Update">
        </div>
    `;
    document.body.appendChild(edit_popup);

    // Añadir event listener al contenedor principal con callback async
    document.querySelector('.main').addEventListener('click', async function(event) {
        if (event.target.classList.contains('btn_edit_task')) {
    
            // Obtener el ID de la tarjeta que contiene el botón pulsado
            const card = event.target.closest('.card');
            const cardId = card ? card.id : 'No ID found';
            console.log(cardId);
            console.log(`Envía get a id: base_url/${cardId}`);
    
            try {
                // Procesa respuesta
                const task = await getTaskById(cardId);
                console.log("Task received:", task);
    
                // Actualizar el párrafo con el ID de la tarjeta
                document.getElementById('task_id').textContent = `Task ID: ${task._id.$oid}`;
                document.getElementById('title').textContent = task.title;
                document.getElementById('description').textContent = task.description;
                document.getElementById('created').textContent = task.createdAt;
                document.getElementById('updated').textContent = task.updateAt;
                
                document.getElementById('edit_popup').style.display = 'block';
            } catch (error) {
                console.error("Error al obtener la tarea:", error);
            }
        }
    });



    document.querySelector('.close-btn').addEventListener('click', function() {
        document.getElementById('edit_popup').style.display = 'none';
    });

    document.querySelector('.update-task-btn').addEventListener('click', function(event) {
        const cardId = document.getElementById('task_id').textContent ;
        console.log(`Envía put a id: base_url/${cardId}`);
    });

    window.addEventListener('click', function(event) {
        if (event.target == document.getElementById('edit_popup')) {
            document.getElementById('edit_popup').style.display = 'none';
        }
    });
});