var user = "xxx";
var token_jwt = "xxx";
var base_url="http://127.0.0.1:3001"

function loadEnviroment(){

    var user = localStorage.getItem("user");
    var token_jwt = localStorage.getItem("token_jwt");

    var miDiv = document.getElementById("user_workspace");
    miDiv.innerText = `${user} Workspace`;
}

loadEnviroment()
