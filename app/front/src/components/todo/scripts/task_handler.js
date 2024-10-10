document.addEventListener('DOMContentLoaded', function() {

	function displayTasks(tasks) {
	    const todoContainer = document.getElementById('toDo');
	    const doingContainer = document.getElementById('doing');
	    const doneContainer = document.getElementById('done');
	    let card_id =0;

	    todoContainer.innerHTML = '';
	    doingContainer.innerHTML = '';
	    doneContainer.innerHTML = '';

	    tasks.forEach(task => {
		card_id = card_id + 1;
		const taskCard = document.createElement('div');
		taskCard.classList.add('task');
		if (task.doing) {
		    taskCard.classList.add('doing');
		    doingContainer.appendChild(taskCard);
		} else if (task.done) {
		    taskCard.classList.add('done');
		    doneContainer.appendChild(taskCard);
		} else {
		    todoContainer.appendChild(taskCard);
		}
		taskCard.innerHTML = `
		    <div class="card" onclick="toggleDescription(this)" id=${task._id.$oid}>
		        <h4>${task.title}</h4>
		        <div class="description" style="display: none;">
		            <p>${task.description}</p>
		        </div>    
		        <div class="doing" style="display: none;">    
		            <p><strong>Doing:</strong> ${task.doing}</p>
		        </div>    
		        <div class="done" style="display: none;">     
		            <p><strong>Done:</strong> ${task.done}</p>
		        </div>    
		        <div class="created" style="display: none;"> 
		            <p><strong>Created At:</strong> ${task.createdAt}</p>
		        </div>    
		        <div class="updated" style="display: none;"> 
		            <p><strong>Updated At:</strong> ${task.updatedAt}</p>
		        </div> 
		        <div class="buttons" style="display: none;">   
		            <br>
		            <button class="btn_edit_task">Edit</button>
		            <button class="btn_rmv_task">Delete</button>
		            <button class="btn_close_task">Close</button>
		        </div>    
		    </div>
		`;
	    });
	}

	getTasksList();
});
