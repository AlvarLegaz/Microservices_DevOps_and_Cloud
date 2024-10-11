document.addEventListener('DOMContentLoaded', function() {
    // Crear el popup y añadirlo al body
    const edit_popup = document.createElement('div');
    edit_popup.id = 'edit_popup';
    edit_popup.className = 'popup';
    edit_popup.innerHTML = `
        <div class="popup-content">
            <span class="close-btn">&times;</span>
            <span id="task_id">Task id</span><br><br>
            <textarea class="input-style" id="title" name="title" rows="2"></textarea><br><br>
            <textarea class="input-style" id="description" name="edit" rows="4"></textarea><br><br>
            <label for="doing_check">Doing:</label>
            <input type="checkbox" class="input-style" id="doing_check" name="do"><br><br>
            <label for="done_check">Done:</label>
            <input type="checkbox" class="input-style" id="done_check" name="do"><br><br>
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

            try {
                // Procesa respuesta
                const task = await getTaskById(cardId);
                console.log("Task received:", task);
    
                // Actualizar el párrafo con el ID de la tarjeta
                document.getElementById('task_id').value = task._id.$oid;
                document.getElementById('title').value = task.title;
                document.getElementById('description').value = task.description;
                document.getElementById('doing_check').checked  = task.doing;
                document.getElementById('done_check').checked  = task.done;
                
                document.getElementById('edit_popup').style.display = 'block';
            } catch (error) {
                console.error("Error al obtener la tarea:", error);
            }
        }
    });

    document.querySelector('.close-btn').addEventListener('click', function() {
        document.getElementById('edit_popup').style.display = 'none';
    });

    document.querySelector('.update-task-btn').addEventListener('click', async function(event) {
        const taskId = document.getElementById('task_id').value ;

        const updated_task = {
            title: document.getElementById('title').value,
            description: document.getElementById('description').value,
            doing: document.getElementById('doing_check').checked,
            done: document.getElementById('done_check').checked 
        };

        console.log(updated_task);
        try {
            let response = await updateTaskById(taskId, updated_task, base_url, user, token_jwt);
            console.log(`Updated request response: /${response}`);
            location.reload();
            
        } catch (error) {
            console.error("Error updating task:", error);
        }
    });

});
