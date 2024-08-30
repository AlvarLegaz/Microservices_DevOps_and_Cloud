function toggleDescription(card) {
    const description = card.querySelector('.description');
    const doing = card.querySelector('.doing');
    const done = card.querySelector('.done');
    const created = card.querySelector('.created');
    const updated = card.querySelector('.updated');
    const buttons = card.querySelector('.buttons');
    const closeButton = card.querySelector('.btn_close_task');
    const editButton = card.querySelector('.btn_edit_task');

    if (description.style.display === 'none') {
        description.style.display = 'block';
        doing.style.display = 'block';
        done.style.display = 'block';
        created.style.display = 'block';
        updated.style.display = 'block';
        buttons.style.display = 'block';
    } 

    closeButton.addEventListener('click', (event) => {
        event.stopPropagation(); // Evita que el evento de clic se propague al contenedor 'card'
        description.style.display = 'none';
        doing.style.display = 'none';
        done.style.display = 'none';
        created.style.display = 'none';
        updated.style.display = 'none';
        buttons.style.display = 'none';

        // Hacer que los campos title, description, doing y done no sean editables
        const title = card.querySelector('input[type="text"]');
        title.readOnly = true;
        description.querySelector('textarea').readOnly = true;

        [doingField, doneField].forEach(field => {
            field.disabled = true;
        });
    });

    editButton.addEventListener('click', (event) => {
        event.stopPropagation();
        showEditPopup(card); // Llama a la función del archivo externo
    });
}
