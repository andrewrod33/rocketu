function myFunction(){
	var view = document.getElementsByClassName("picklist");
	view[0].style.display = 'none';
}

function doSomething(element){
	var list = document.getElementsByClassName(element.name),
			showList = (element.checked === true),
			displayStyle = 'none';
	if (showList){
		displayStyle = 'block';
	}
	for(var i=0; i<list.length; i++){
		list[i].style.display= displayStyle;
		}
} 

function toggleNewItems(newItemsButton) {
	var newMovieItems = document.getElementsByClassName('new');
	var buttonText = newItemsButton.textContent || newItemsButton.innerText;

	if (buttonText === "Highlight new movies") {
		var textColor = "white";
		var bgColor = "green";
		newItemsButton.textContent = "Unhighlight new movies";
	} else {
		var textColor = "black";
		var bgColor = "transparent";
		newItemsButton.textContent = "Highlight new movies";
	}

	for(var i=0; i < newMovieItems.length; i++) {
	    newMovieItems[i].style.color = textColor;
	    newMovieItems[i].style.background = bgColor;
	}	
}

function addMovieToPickList(listItem) {
	document.getElementsByClassName("picklist")[0].style.display = "block";	
	document.getElementById("startnote").style.display = "none";	
    
    var pickList = document.getElementsByClassName("picklist")[0];
    
    var newItem = document.createElement("li");
    var itemText = document.createTextNode(listItem.textContent);
    
    newItem.appendChild(itemText);
    pickList.appendChild(newItem);		
}