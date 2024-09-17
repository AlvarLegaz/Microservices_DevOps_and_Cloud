var user = "alvar";
var base_url="http://127.0.0.1:3001"

function loadEnviroment(){

    var miDiv = document.getElementById("user_workspace");
    miDiv.innerText = `${user} Workspace`;
}

loadEnviroment()