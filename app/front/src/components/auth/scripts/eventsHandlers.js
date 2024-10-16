document.addEventListener('DOMContentLoaded', function() {
	
	let redirectUrl='';
	let apiKey='';
	let loginServiceBaseUrl='';
	let loginEndpoint='';
	let registerEndpoint='';

    // Cargar config.json al cargar la página
    fetch('config.json')
        .then(response => response.json())
        .then(configData => {
            
			apiKey = configData.login_apiKey;
			
			loginServiceBaseUrl = `${configData.login_service_base_url}:${configData.login_service_base_port}`;
			loginEndpoint = configData.login_service_endpoint;
			registerEndpoint = configData.register_service_endpoint;
			
			redirectUrl = configData.redirect_url_after_login_ok;
			
			console.log("login service base url:" + loginServiceBaseUrl);
			
        })
        .catch(error => {
            console.error('Error al leer el archivo config.json:', error);
        });

	document.getElementById('loginForm').addEventListener('submit', async function(event) {
		
		event.preventDefault();
		const user = document.getElementById('username').value;
		const password = document.getElementById('password').value;
		const loginUrl = `${loginServiceBaseUrl}${loginEndpoint}`;
		console.log("login endpoint:" + loginUrl);
		
		try{
			let response = await login(user, password, loginUrl, apiKey)
			let token_jwt = response.access_token;
			console.log('Login Success:', token_jwt);
			localStorage.setItem("user", user);
			localStorage.setItem("token_jwt", token_jwt);
			window.location.href = redirectUrl;
		}
		catch(error){
			console.error('Login Error:', error);
			showMessage('Error en el login:',error.message);
		}
	});

	document.getElementById('registerForm').addEventListener('submit', async function(event) {
		
		event.preventDefault();
		const newUser = document.getElementById('newUsername').value;
		const newPassword = document.getElementById('newPassword').value;
		const registerUrl = `${loginServiceBaseUrl}${registerEndpoint}`;

		const data = { user: newUser, password: newPassword };
		console.log('Register body:', data);
		
		try{
			response = await register(newUser, newPassword, registerUrl, apiKey)
			console.log('Register Success:', response);
		}
		catch(error){
			console.error('Register Error:', error);
			showMessage('Error in register:',error.message);
		}

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
