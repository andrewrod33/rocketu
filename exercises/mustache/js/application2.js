$(document).ready(function(){

	$.ajax(
		{
			url: 'http://bootcamp-rocketu.rhcloud.com/exercises/ajax/data/places-cafe.json',
			//url: 'http://bootcamp-rocketu.rhcloud.com/exercises/ajax/data/movies-box-office.json',
			type: 'GET',
			dataType: 'json',
			data:{},
			success: function(json) {
				console.log(json);

			//$('ul#list').html(Mustache.render($("#all-cafe-template").html(), json  )
				//)

			}
		}
	);



});