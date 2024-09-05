document.addEventListener('DOMContentLoaded', function() {
    // Crear el popup y añadirlo al body
    const edit_popup = document.createElement('div');
    edit_popup.id = 'edit_popup';
    edit_popup.className = 'popup';
    edit_popup.innerHTML = `
        <div class="popup-content">
            <span class="close-btn">&times;</span>
            <div>
                <label class="label-element" id="task_id">Task id</label><br><br>

                <label class="label-element" for="title">Título:</label>
                <textarea class="input-style" id="title" name="title" rows="2"></textarea><br><br>

                <label class="label-element" for="description">Description:</label>
                <textarea class="input-style" id="description" name="edit" rows="4"></textarea><br><br>

                <input type="submit" class="update-task-btn" value="Update">
            </div>
        </div>
    `;
    document.body.appendChild(edit_popup);

    // Añadir event listener al contenedor principal
    document.querySelector('.main').addEventListener('click', function(event) {
        if (event.target.classList.contains('btn_edit_task')) {

            // Obtener el ID de la tarjeta que contiene el botón pulsado
            const card = event.target.closest('.card');
            const cardId = card ? card.id : 'No ID found';
            console.log(cardId);
            console.log(`Envía get a id: base_url/${cardId}`);

            // Procesa respuesta
            const task = getTaskById(cardId)
            console.log(task);

            // Actualizar el párrafo con el ID de la tarjeta
            document.getElementById('task_id').textContent = task.id;
            document.getElementById('title').textContent = task.title;
            document.getElementById('description').textContent = task.description;
            
            document.getElementById('edit_popup').style.display = 'block';
        }
    });

    document.querySelector('.close-btn').addEventListener('click', function() {
        document.getElementById('edit_popup').style.display = 'none';
    });

    document.querySelector('.update-task-btn').addEventListener('click', function(event) {
        const card = event.target.closest('.card');
        const cardId = card ? card.id : 'No ID found';
        console.log(`Envía put a id: base_url/${cardId}`);
    });

    window.addEventListener('click', function(event) {
        if (event.target == document.getElementById('edit_popup')) {
            document.getElementById('edit_popup').style.display = 'none';
        }
    });
});