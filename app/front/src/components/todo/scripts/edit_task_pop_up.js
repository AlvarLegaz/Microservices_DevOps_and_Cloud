document.addEventListener('DOMContentLoaded', function() {
    // Crear el popup y añadirlo al body
    const edit_popup = document.createElement('div');
    edit_popup.id = 'edit_popup';
    edit_popup.className = 'popup';
    edit_popup.innerHTML = `
        <div class="popup-content">
            <span class="close-btn">&times;</span>
            <p id="edit_message">Tarea editada</p>
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

            // Actualizar el párrafo con el ID de la tarjeta
            document.getElementById('edit_message').textContent = `Tarea editada: ${cardId}`;

            document.getElementById('edit_popup').style.display = 'block';
        }
    });

    document.querySelector('.close-btn').addEventListener('click', function() {
        document.getElementById('edit_popup').style.display = 'none';
    });

    window.addEventListener('click', function(event) {
        if (event.target == document.getElementById('edit_popup')) {
            document.getElementById('edit_popup').style.display = 'none';
        }
    });
});