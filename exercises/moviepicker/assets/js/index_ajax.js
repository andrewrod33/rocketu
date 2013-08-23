$(document).ready(function(){
	//var category2 = $(this).find('movies#category').val();
	//var  title1 = $(this).find('movies#title').val();

	$.ajax(
			{
				url: 'http://bootcamp-rocketu.rhcloud.com/exercises/moviepicker/assets/data/movies.json',
				type: 'GET',
				dataType: 'json',
				data:{
					//category: category2,
					//title: title1
				},
				success: function(title,isTrue,category) {
					console.log(title,isTrue,category);
					// for(var k in json.movies){
					// $('body').append('<p>' + k + '=' + json.movies + '</p>')
					// }
				
				}	
			}
			)
	//console.log(category2);
});