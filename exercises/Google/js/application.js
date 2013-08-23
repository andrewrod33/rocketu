function errorHandler(){
	console.log('Error');
}



if (navigator.geolocation){
	navigator.geolocation.getCurrentPosition(
		function(position){
			var lat = position.coords.latitude;
			var lng = position.coords.longitude;
		
			url = getStaticMapUrl(position.coords);
			console.log(url);
			drawMap(url);

	}, errorHandler);
}else {
	//Sorry, Geolocation is not supported
}

function getStaticMapUrl(params) {
	var url = 'http://maps.googleapis.com/maps/api/staticmap?',
		options = {
			zoom: 15,
			sensor: false,
			size: '300x300',
			key: 'AIzaSyDuiqjtORQSJr1cTdjMWh8Q66xpKfOojQA'	
		};
	if (params.latitude && params.longitude) {
		options.center = params.latitude + ',' + params.longitude;
	} else {
		options.center = 'San Francisco, CA';
	}
	for(var i in options) {
		url += i + '=' + encodeURI(options[i]) + '&';
	}
	return url;
}
function drawMap(url) {
	var map = document.getElementById('static-map');
	map.innerHTML = '<img src="' + url + '"/>';
}


function getDynamicMap(position) {
	var mapOptions = {
		center: new google.maps.LatLng(37.797677,-122.394339),
		zoom: 15,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	};
	var map = new google.maps.Map(
		document.getElementById("dynamic-map"),
		mapOptions
		);
}	
	google.maps.event.addDomListener(window, 'load', getDynamicMap);

var map;

function initialize() {
  var mapOptions = {
    zoom: 15,
    mapTypeId: google.maps.MapTypeId.TERRAIN
  };
  map = new google.maps.Map(document.getElementById('dynamic-map'),
      mapOptions);


  if(navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = new google.maps.LatLng(position.coords.latitude,
                                       position.coords.longitude);

      var infowindow = new google.maps.InfoWindow({
        map: map,
        position: pos,
        content: 'Moms'
      });

      map.setCenter(pos);
    }, function() {
      handleNoGeolocation(true);
    });
  } else {
    // Browser doesn't support Geolocation
    handleNoGeolocation(false);
  }
}

function handleNoGeolocation(errorFlag) {
  if (errorFlag) {
    var content = 'Error: The Geolocation service failed.';
  } else {
    var content = 'Error: Your browser doesn\'t support geolocation.';
  }

  var options = {
    map: map,
    position: new google.maps.LatLng(60, 105),
    content: content
  };

  var infowindow = new google.maps.InfoWindow(options);
  map.setCenter(options.position);
}

google.maps.event.addDomListener(window, 'load', initialize);
