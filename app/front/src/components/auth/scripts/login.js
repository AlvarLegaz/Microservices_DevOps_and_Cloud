document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const user = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const data = { user, password };
    console.log('Login body:', data);

    fetch('http://127.0.0.1:3000/login', {
        method: 'POST',
        headers: {
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
        console.log('Login Success:', data);
        alert('Goes to selected url');
    })
    .catch((error) => {
        console.error('Login Error:', error);
        showMessage('Error en el login:',error.message);
    });
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