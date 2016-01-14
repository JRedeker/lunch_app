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
	  

		latitude = "39";
		longitude = "-77";
		options = "chinese";
		distance = "5";
		resultsLimit = "1";

		
		$.ajax({
			method: "POST",
			data:{"latitude":latitude, "longitude":longitude, "options":options,
				  "distance":distance,"resultsLimit":resultsLimit},
			url: "api/1/getYelpData",
			success:function(data) {				

				console.log(data);

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
