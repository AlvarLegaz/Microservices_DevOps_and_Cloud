document.addEventListener('DOMContentLoaded', function() {
    // Crear el popup y añadirlo al body
    const popup = document.createElement('div');
    popup.id = 'popup';
    popup.className = 'popup';
    popup.innerHTML = `
        <div class="popup-content">
            <span class="close-btn">&times;</span>
            <p>Tarea añadida</p>
        </div>
    `;
    document.body.appendChild(popup);

    // Añadir event listener al contenedor principal
    document.querySelector('.main').addEventListener('click', function(event) {
        if (event.target.classList.contains('btn_add_task')) {
            document.getElementById('popup').style.display = 'block';
        }
    });

    document.querySelector('.close-btn').addEventListener('click', function() {
        document.getElementById('popup').style.display = 'none';
    });

    window.addEventListener('click', function(event) {
        if (event.target == document.getElementById('popup')) {
            document.getElementById('popup').style.display = 'none';
        }
    });
});