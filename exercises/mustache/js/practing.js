$(document).ready(function(){

	$.ajax(
	{
		url: 'test.com',
		type: 'GET',
		dataType: 'json',
		data: {},
		success: function(json){
			console.log(json);
		}







	});

}):