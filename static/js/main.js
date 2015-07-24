$(window).scroll(function() {
	if ($(".navbar").offset().top > 50) {
	  $(".navbar-fixed-top").removeClass("navbar-custom");
	} else {
	  $(".navbar-fixed-top").addClass("navbar-custom");
	}
});

$('nav ul li a').click(function(){ 
	href = $(this).attr('href');
	// href = href.replace('#', '');
	if($('h3'+href).hasClass('ui-state-default')){
	  $('h3'+href).trigger('click');
	}
});

$('#multiOpenAccordion').multiAccordion({active: [0]});
$("#back-top").hide();
$(window).scroll(function () {
	if ($(this).scrollTop() > 100) {
	  $('#back-top').fadeIn();
	} else {
	  $('#back-top').fadeOut();
	}
});

$('#back-top a').click(function () {
	$('html, body').animate({ scrollTop:0 }, "slow");
});
// $('[data-toggle="tooltip"]').tooltip({ html: true });