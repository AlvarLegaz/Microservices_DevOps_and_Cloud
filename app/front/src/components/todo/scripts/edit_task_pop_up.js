document.addEventListener('DOMContentLoaded', function() {
    // Crear el popup y añadirlo al body
    const edit_popup = document.createElement('div');
    edit_popup.id = 'edit_popup';
    edit_popup.className = 'popup';
    edit_popup.innerHTML = `
        <div class="popup-content">
            <span class="close-btn">&times;</span>
            <div>
                <label id="task_id">Task id</label><br><br>

                <label for="title">Título:</label>
                <textarea id="title" name="title"></textarea><br><br>

                <label for="description">Description:</label>
                <textarea id="description" name="edit"></textarea><br><br>

                <input type="submit" class="update_task" value="Update">
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

            // Actualizar el párrafo con el ID de la tarjeta
            document.getElementById('task_id').textContent = `Task ID: ${cardId}`;
            document.getElementById('title').textContent = `Tarea editada: ${cardId}`;
            document.getElementById('description').textContent = `Tarea editada: ${cardId}`;
            
            document.getElementById('edit_popup').style.display = 'block';
        }
    });

    document.querySelector('.close-btn').addEventListener('click', function() {
        document.getElementById('edit_popup').style.display = 'none';
    });

    document.querySelector('.update_task').addEventListener('click', function(event) {
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