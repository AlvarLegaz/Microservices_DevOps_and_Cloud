document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const user= document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const data = { user, password };
    console.log('body:', data);		

    fetch('http://192.168.18.64:3000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
	mode: 'cors', // Ensure this is set to 'cors'
        body: JSON.stringify(data)
	
    })
    .then(response => response.json())
    .then(data => {
        console.log('Response:', data);
        // Aquí puedes manejar la respuesta del servidor
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
