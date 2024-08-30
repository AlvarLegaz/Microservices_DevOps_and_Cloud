function showEditPopup(card) {
    // Crear el contenedor del pop-up
    const popup = document.createElement('div');
    popup.classList.add('popup');

    // Añadir contenido al pop-up
    popup.innerHTML = `
        <div class="popup-content">
            <h2>Edit Task</h2>
            <label>Title:</label>
            <input type="text" value="${card.querySelector('input[type="text"]').value}">
            <label>Description:</label>
            <textarea>${card.querySelector('textarea').value}</textarea>
            <label>Doing:</label>
            <select>
                <option value="true" ${card.querySelector('.doing select').value === 'true' ? 'selected' : ''}>True</option>
                <option value="false" ${card.querySelector('.doing select').value === 'false' ? 'selected' : ''}>False</option>
            </select>
            <label>Done:</label>
            <select>
                <option value="true" ${card.querySelector('.done select').value === 'true' ? 'selected' : ''}>True</option>
                <option value="false" ${card.querySelector('.done select').value === 'false' ? 'selected' : ''}>False</option>
            </select>
            <button onclick="closePopup()">Close</button>
        </div>
    `;

    // Añadir el pop-up al cuerpo del documento
    document.body.appendChild(popup);
}

function closePopup() {
    const popup = document.querySelector('.popup');
    if (popup) {
        popup.remove();
    }
}
