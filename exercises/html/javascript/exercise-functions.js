function sayHello(){
	alert(getGreeting()+" world");
}

function getGreeting(){
	var d = new Date();
	var n = d.getHours();
	var greeting;
	if (n < 12){
		greeting='Good Morning';
	}else{
		greeting='Good Evening';
	}
return greeting;
}


function getUserName(){
	var userName = window.prompt("Hi,What is your name?", " ");
	//document.getElementById("msg").innerHTML= "Greetings " + userName;
	
	return userName;
}

function sayPersonalHello(){
	var userName= getUserName();
	var message = getGreeting();
	if (userName.length== 0){
		alert("Sorry, I don't talk to Strangers");
		return;
	}else{
		var r = confirm(message+ "," + userName +"," + "how are you?\n"+"Would you like to like this added to your page?")
	}
	if (r == true){
		document.getElementById("greeting").innerHTML= message + " "+userName
	}
}

/*function doTimesTables(){
	prompt("Please enter a number from 1 to 10", "5")
	if (){}
}*/
