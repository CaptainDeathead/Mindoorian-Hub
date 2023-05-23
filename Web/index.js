function send(){
    var chat = document.getElementById("chat").value;
    if(chat == ""){
        alert("Please enter a message");
        return false;
    }
    else{
        var chatlog = document.getElementById("chatlog");
        var p = document.createElement("p");
        p.innerHTML = username + ": " + chat;
        chatlog.appendChild(p);
        document.getElementById("chat").value = "";
        return true;
    }
}

// check when the window is loaded
window.onload = function(){
    var loggenIn = false;
    var username = "";

    // check if the user is not logged in
    if(loggenIn == false){
        // hide the chatlog and chatbox
        document.getElementById("chatlog").style.display = "none";
        document.getElementById("chatbox").style.display = "none";

        // show the login form
        document.getElementById("login").style.display = "block";
    }
    else{
        // hide the login form
        document.getElementById("login").style.display = "none";

        // show the chatlog and chatbox
        document.getElementById("chatlog").style.display = "block";
        document.getElementById("chatbox").style.display = "block";
    }
}

function login(){
    // get the username
    var username = document.getElementById("username").value;

    // make the username global
    window.username = username;

    // check if the username is empty
    if(username == ""){
        alert("Please enter a username");
        return false;
    }
    else{
        // hide the login form
        document.getElementById("login").style.display = "none";

        // show the chatlog and chatbox
        document.getElementById("chatlog").style.display = "block";
        document.getElementById("chatbox").style.display = "block";
        return true;
    }
}