document.addEventListener('DOMContentLoaded', function() {
    // Crear el popup y añadirlo al body
    const popup = document.createElement('div');
    popup.id = 'popup';
    popup.className = 'popup';
    popup.innerHTML = `
        <div class="popup-content">
            <span class="task_close-btn">&times;</span>
            <span id="task_id"><h2>New Task</h2></span><br><br>
            <div>
                <h3>Title</h3>
                <textarea class="input-style" id="create_task_title" name="title" rows="2"></textarea><br><br>
            </div>
            <div>
                <h3>Description</h3>
                <textarea class="input-style" id="create_task_description" name="edit" rows="4"></textarea><br><br>
            </div>
            <div style="display: none;">
                <input type="checkbox" class="input-style" id="create_task_doing_check" name="do">
                <input type="checkbox" class="input-style" id="create_task_done_check" name="do">
            </div>
            <input type="submit" class="create-task-btn"value="Create">
        </div>
    `;
    document.body.appendChild(popup);

    // Añadir event listener al contenedor principal
    document.querySelector('.main').addEventListener('click', function(event) {
        if (event.target.id.includes('add_pending_task')){
            console.log('Add pending task')
            document.getElementById('create_task_doing_check').checked = false;
            document.getElementById('create_task_done_check').checked = false;
            document.getElementById('popup').style.display = 'block';
        }
        if (event.target.id.includes('add_doing_task')){
            document.getElementById('create_task_doing_check').checked = true;
            document.getElementById('create_task_done_check').checked = false;
            console.log('Add doing task')
            document.getElementById('popup').style.display = 'block';
        }
        if (event.target.id.includes('add_blocked_task')){
            console.log('Add blocked task')
            document.getElementById('popup').style.display = 'block';
        }
        if (event.target.id.includes('add_done_task')){
            document.getElementById('create_task_doing_check').checked = false;
            document.getElementById('create_task_done_check').checked = true;
            console.log('Add done task')
            document.getElementById('popup').style.display = 'block';
        }
        
    });

    document.querySelector('.create-task-btn').addEventListener('click', async function(event) {
    
        const created_task = {
            title: document.getElementById('create_task_title').value,
            description: document.getElementById('create_task_description').value,
            doing: document.getElementById('create_task_doing_check').checked,
            done: document.getElementById('create_task_done_check').checked 
        };

        console.log(created_task);
        try {
            let response = await createTask(created_task);
            console.log(`Updated request response: /${response}`);
            location.reload();
            
        } catch (error) {
            console.error("Error updating task:", error);
        }
    });

    document.querySelector('.task_close-btn').addEventListener('click', function() {
        document.getElementById('popup').style.display = 'none';
    });

});