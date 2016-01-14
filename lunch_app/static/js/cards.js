$( document ).ready(function() {

	$('#fromhere').click(function() {

		console.log("clicked");

		
		/*
		$('#go-card').css("display", "block");
		$('#foodtype-card').css("display", "block");
		$('#distance-card').css("display", "block");
		$('#description-card').css("display", "block");
		$('#distance-card').css("display", "block");
		*/
		/*
		$('#go-card').toggle(500);
		$('#foodtype-card').toggle(500);
		*/
		$('#description-card').slideToggle(750);
		$('#distance-card').slideToggle(750);
		$('#foodtype-card').slideToggle(750);
		$('#go-card').slideToggle(750);

		$('#getstarted-card').css("display", "none");
	});

	/*
	$("#fromhere").click(function (){ 
        $('main').animate({
            scrollTop: $("#gohere").offset().top - 65
        }, 1000);
    });
*/

});