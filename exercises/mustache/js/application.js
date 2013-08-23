//http://bootcamp-rocketu.rhcloud.com/exercises/ajax/data/movies-box-office.json
$(document).ready(function(){

	$.ajax(
		{
			url: 'http://bootcamp-rocketu.rhcloud.com/exercises/ajax/data/movies-box-office.json',
			type: 'GET',
			dataType: 'json',
			data:{},
			success: function(json) {
				console.log(json);

				/*for(var i in json.movies){
						$('#add').append('<li>' + json.movies[i].title +'</li>');
				
				var movieOldTemplate='<li>Title: {{title}} <br>Rating: {{ratings.audience_score}} <br>Release Date: {{release_dates.theater}}</li>';

				
				var output = Mustache.render(movieTemplate, json.movies[i]);

				var movieTemplate = $('#movie-template').html();

				$('body').append( output );*/

			
				}
			}
		}
	);



});