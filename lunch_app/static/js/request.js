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
	  

		
		$.ajax({
			method: "POST",
			url: "api/1/getYelpData",
			success:function(data) {
				console.log( JSON.stringify(data, null, 2) ); 
				var name = jQuery.parseJSON( '{ "name": "John" }' );

				//console.log("JSON PARSE: " + data["name"]);

				$( "#result1").css( "display", "block" );

				$( "#result1content" ).append("<h2>" +  data["name"] + "</h2>" );

				$( "#result1content" ).append("<div>" + data["street address"][0] + "</br>" + data["city"] + ", " + data["state"] + " " + data["postal_code"] + "</div>" );

				$( "#result1content" ).append("<img src='" + data["image_url"] + "'/>" );
   	   		}
		})
		  

	  	
	});

});



// Allow Bootstrap dropdown menus to have forms/checkboxes inside, 
// and when clicking on a dropdown item, the menu doesn't disappear.
$(document).on('click', '.dropdown-menu.dropdown-menu-form', function(e) {
  e.stopPropagation();
});
