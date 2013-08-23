$(document).ready(function() {
	$('form').on('submit',function(){
		var firstname = $(this).find('input#firstname').val();
		var lastname = $(this).find('input#lastname').val();
		
		$.ajax(
			{
				url: 'http://bootcamp-rocketu.rhcloud.com/api',
				//type: 'GET',
				dataType: 'json',
				data:{
					firstname: firstname,
					lastname: lastname,
					date: (new Date())
				},
				success: function(json) {
					console.log(json);
				}
			}



		);
		console.log(firstname + ' '+ lastname);
		return false;
	});

	$('#getjson').click(function() {
		var me = {
			firstname: 'Andrew', 
			lastname:'Rodriguez', 
			email: 'andrewrodriguez2012@gmail.com',
			address:'303 Adams St',
			age: 28,
			cell: '5104592120',
			bands:['Intocable','Ramon Ayala']
		};
		console.log('Hi my name is '+ me.firstname + '.' + ' I\'m ' + me.age + ' years old and I like to listen to '+ me.bands[0] + '.');
		});
	
	$('#getxml').on('click',function(){
			var personxml = "<?xml version = '1.0'?>";
					personxml +="<person>";
					personxml +="	<firstname>Andrew</firstname>";
					personxml +="	<lastname>Rodriguez</lastname>";
					personxml +="	<age>28</age>";
					personxml +="	<bands><band>Intocable</band><band>Ramon Ayala</band></bands>";
					personxml +="</person>";
			var xmlDoc = $.parseXML(personxml);
	 		var xml = $(xmlDoc);

	 			var firstname = xml.find("firstname").text();
	 				lastname = xml.find("lastname").text();
	 				age= xml.find("age").text();
	 				band= xml.find("bands band").first().text();

	 		console.log('Hi I\'m ' +firstname +'.'+ " I\'m "+age+ ' years old and I like to listening to '+ band+'.')
	});

	/*$('#getjsonajax').on('click',function() {
			$.ajax({
				url: 'data/me.json',
				dataType: 'json',
				success: function(data) {
					console.log(data);

					var msg = 'Hi, I\'m ' + data.firstname + '. ';
					msg += 'I\'m ' + data.age + ' years old and ';
					msg += 'my cell number is ' + data.cell + '. ';
					msg += 'Here\'s a list of bands that I like:';

					$('body').append( $('<p/>').html(msg) );

					list = $('<ul/>');
					for(var i=0; i<data.bands.length; i++) {
						list.append( $('<li/>').html(data.bands[i]) );	
					}
					$('body').append(list);
				}
			});*/

/*	$('#getxmlajax').on('click',function() {
		$.ajax({
   			url: 'data/my-data.xml',
   			dataType: 'xml',
   			success: function(person){
     			var firstname = $(person).find("firstname").text();
     				lastname = $(person).find("lastname").text();
     				age = $(person).find("age").text();
     				band = $(person).find("bands band").first().text();

     	console.log('Hi I\'m ' + firstname +'. I\'m ' + age + ' years old and my cell number is '+ cell +'. Here\'s a list of bands that I like.');
   }
});

	});*/

	$('#testGet').on('click',function() {
		$.ajax({
			url: 'http://bootcamp-rocketu.rhcloud.com/api?submit=Submit&firstname=Andrew&lastname=Rodriguez&age=28',
			type: 'GET',
			dataType: 'json',
			success: function(data) {
				console.log(data);

				for(var k in data.data){
					$('body').append('<p>' + k + '=' + data.data[k] + '</p>');
				}
				}
			});
		});
	});
	



	/*$('#getmovie').on('click',function(){
		console.log('Getting movie');

		$.ajax({
			url:'data/movie.json',
			dataType:'json',
			success: function(data){
				console.log(data);
				//option 1
				for (i=0; i<data.length; i++){
					$('body').append( $('</p>').html(data[i].title) );
				}
			}

	
		});
	});
});*/
