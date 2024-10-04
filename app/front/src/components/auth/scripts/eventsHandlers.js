document.addEventListener('DOMContentLoaded', function() {
	
	let redirectUrl = ''
	let apiKey = '';
	let loginServiceBaseUrl = 'http://127.0.0.1:3000/';
	let loginEndpoint = '/login';
	let registerEndpoint = '/register';

    // Cargar config.json al cargar la página
    fetch('/auth/config.json')
        .then(response => response.json())
        .then(configData => {
            redirectUrl = configData.redirect_url_after_login_ok;
			apiKey = configData.login_apiKey;
        })
        .catch(error => {
            console.error('Error al leer el archivo config.json:', error);
        });

	document.getElementById('loginForm').addEventListener('submit', async function(event) {
		
		event.preventDefault();
		const user = document.getElementById('username').value;
		const password = document.getElementById('password').value;
		const loginUrl = `${loginServiceBaseUrl}${loginEndpoint}`;
		
		try{
			token_jwt = await login(user, password, loginUrl, apiKey)
			console.log('Login Success:', token_jwt);
			localStorage.setItem("user", user);
			localStorage.setItem("token_jwt", token_jwt);
		}
		catch(error){
			console.error('Login Error:', error);
			showMessage('Error en el login:',error.message);
		}
	});

	document.getElementById('registerForm').addEventListener('submit', function(event) {
		event.preventDefault();
		const newUser = document.getElementById('newUsername').value;
		const newPassword = document.getElementById('newPassword').value;

		const data = { user: newUser, password: newPassword };
		console.log('Register body:', data);

		fetch('http://127.0.0.1:3000/register', {
			method: 'POST',
			headers: {
				'X-Hash': apiKey,
				'Content-Type': 'application/json'
			},
			mode: 'cors',
			body: JSON.stringify(data)
		})
		.then(response => {
			if (!response.ok) {
				return response.json().then(errorData => {
					throw new Error(JSON.stringify(errorData));
				});
			}
			return response.json();
		})
		.then(data => {
			console.log('Register completed: ', data);
			showMessage('Success!','Register completed');
		})
		.catch((error) => {
			console.error('Registration error Error:', error);
			showMessage('Registration error:', error.message);
		});
	});

	function showMessage(title, message) {
		const messageContainer = document.getElementById('message-container');
		const messageTitle = document.getElementById('message-title');
		const messageContent = document.getElementById('message-content');
		
		messageTitle.textContent = title;
		messageContent.textContent = message;
		messageContainer.style.display = 'block';
	}

	document.getElementById('close-message').addEventListener('click', function() {
		const messageContainer = document.getElementById('message-container');
		messageContainer.style.display = 'none';
	});

	document.getElementById('showRegisterForm').addEventListener('click', function() {
		const loginContainer = document.getElementById('login-container');
		const registerContainer = document.getElementById('register-container');

		loginContainer.style.display = 'none';
		registerContainer.style.display = 'block'; 
	});

	document.getElementById('showLoginForm').addEventListener('click', function() {
		const loginContainer = document.getElementById('login-container');
		const registerContainer = document.getElementById('register-container');

		registerContainer.style.display = 'none';
		loginContainer.style.display = 'block';
	});
});