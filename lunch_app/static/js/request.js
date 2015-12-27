// This is a function to talk to the backend python with expected params
function sendRequest(n) {

	var lat = lat;
	var lon = lon;
	var numberOfPlaces = n;
	var radius = $("#distanceOpt");

	console.log(lat + " " + lon + " " + numberOfPlaces + " " + " " + radius)

}

// Allow Bootstrap dropdown menus to have forms/checkboxes inside, 
// and when clicking on a dropdown item, the menu doesn't disappear.
$(document).on('click', '.dropdown-menu.dropdown-menu-form', function(e) {
  e.stopPropagation();
});