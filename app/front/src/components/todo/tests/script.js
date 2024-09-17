// Crear el HTML de la ventana emergente y el overlay
const popupHTML = `
    <div id="overlay" class="overlay"></div>
    <div id="popup" class="popup">
        <h2>Ventana Emergente</h2>
        <p>Este es el contenido de la ventana emergente.</p>
        <button id="closePopupBtn">Cerrar</button>
    </div>
`;

// Insertar el HTML en el body
document.body.insertAdjacentHTML('beforeend', popupHTML);

// Obtener elementos
const openPopupBtn = document.getElementById('openPopupBtn');
const closePopupBtn = document.getElementById('closePopupBtn');
const popup = document.getElementById('popup');
const overlay = document.getElementById('overlay');

// Función para abrir la ventana emergente
openPopupBtn.addEventListener('click', () => {
    popup.classList.add('open');
    overlay.classList.add('open');
});

// Función para cerrar la ventana emergente
closePopupBtn.addEventListener('click', () => {
    popup.classList.remove('open');
    overlay.classList.remove('open');
});

// Cerrar la ventana emergente al hacer clic en el overlay
overlay.addEventListener('click', () => {
    popup.classList.remove('open');
    overlay.classList.remove('open');
});
