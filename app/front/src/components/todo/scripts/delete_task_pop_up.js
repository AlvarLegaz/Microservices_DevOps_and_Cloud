document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('.main').addEventListener('click', async function(event) {
        if (event.target.classList.contains('btn_rmv_task')) {
    
            // Obtener el ID de la tarjeta que contiene el botón pulsado
            const card = event.target.closest('.card');
            const cardId = card ? card.id : 'No ID found';
            console.log(cardId);
            console.log(`Envía delete a id: base_url/${cardId}`);

            try {
                let response = await deleteTaskById(cardId, base_url, user, token_jwt);
                console.log(`Delete request response: /${response}`);
                location.reload();
                
            } catch (error) {
                console.error("Error al elimiar la tarea:", error);
            }
        }
    });
    
});
