$(document).ready(function() {
	$('#picklist ul.picklist').hide();
	
	$('input[type=checkbox]').on('change',function() {

		var name = ( $(this).attr('name') );

		//console.log(this)
		/*For this I want to listen to the checkboxes to see if they are clicked
		or not. Once I understand that I need to figure our how to hide those*/
	$('.'+ name ).toggle();
		});

$('button#btn-newmovies').on('click',function() {
		var btnText = $(this).text();
		if (btnText == 'Highlight new movies') {
   			$("li.new").css('background-color', 'lightgreen');
   			$(this).text('Remove highlights');
		}else {
			$("li.new").css('background-color', 'transparent');
			$(this).text('Highlight new movies');
		}
		
$("#picklist ul").append();
	});

});
