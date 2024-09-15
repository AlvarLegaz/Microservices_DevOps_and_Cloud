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
    .then(response => response.json())
    .then(data => console.log('Login Success:', data))
    .catch((error) => console.error('Login Error:', error));
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
    .then(response => response.json())
    .then(data => console.log('Register Success:', data))
    .catch((error) => console.error('Register Error:', error));
});

document.getElementById('showRegisterForm').addEventListener('click', function() {
    const loginContainer = document.querySelector('.login-container .row:nth-child(1)');
    const registerContainer = document.getElementById('registerContainer');

    if (registerContainer.style.display === 'none') {
        registerContainer.style.display = 'block';
        loginContainer.style.display = 'none';
    } else {
        registerContainer.style.display = 'none';
        loginContainer.style.display = 'block';
    }
});


