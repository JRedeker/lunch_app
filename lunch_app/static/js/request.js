// This is a function to talk to the backend python with expected params
function sendRequest(n) {

	var lat = lat;
	var lon = lon;
	var numberOfPlaces = n;
	var radius = $("#distanceOpt");

	console.log(lat + " " + lon + " " + numberOfPlaces + " " + " " + radius)

}




$( document ).ready(function() {
    $( "#chooseforme" ).click(function() {
	  console.log( "lol" );

		
		$.ajax({
			method: "POST",
			url: "http://localhost:8080/api/1/getYelpData",
			success:function(data) {

				console.log( JSON.stringify(data, null, 2) ); 

      		}
		})
		  

	  	
	});

});



// Allow Bootstrap dropdown menus to have forms/checkboxes inside, 
// and when clicking on a dropdown item, the menu doesn't disappear.
$(document).on('click', '.dropdown-menu.dropdown-menu-form', function(e) {
  e.stopPropagation();
});