function login() {
	    	console.log('Welcome!  Fetching your information.... ');
	    	getMe();
	    	getFriends();
	    	getMusic();
}


function getMe(){
	FB.api('/me', function(response) {
		console.log(response);
		console.log('Good to see you, ' + response.name + '.');
		name = response.name;

		if (!response.username || response.username === '') {
			response.username = response.id;
		}

		imgSrc = 'http://graph.facebook.com/' + response.username + '/picture?type=large';
		$('body').append( $('<h1/>').html(name) );
		$('body').append( $('<img/>').attr('src',imgSrc) );

	});
}
function getFriends(){
	  	 	FB.api('/me/friends', function(response) {
	        	console.log('Getting Friends');
	        	console.log(response)
	    	});
		}

function getMusic(){
	  	 	FB.api('/me/music', function(response) {
	        	console.log('Getting Music');
	        	console.log(response)
	    	});
		}




$(document).ready(function(){
	$('#logout').on('click',function(){
		FB.logout(function(response) {
  // user is now logged out
  			console.log(response)
		});
	});
});