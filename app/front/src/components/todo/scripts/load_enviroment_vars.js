async function loadEnviroment() {
    // Asignar las variables al objeto global window
    base_url = "http://127.0.0.1:3001";
    user = localStorage.getItem("user");
    token_jwt = localStorage.getItem("token_jwt");
    
    var miDiv = document.getElementById("user_workspace");
    miDiv.innerText = `${window.user} Workspace`;
}

