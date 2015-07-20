$('[data-toggle="tooltip"]').tooltip({ html: true });
// $("body").on("click", function(){ 
// 	dismissRelatedObjectPopup() 
// });
$('#searchbar').keydown(function(e){ 
	if( e.which == '13' ){
	  $("#changelist-search").submit(); 
	}
});
$('#searchbar').yourlabsAutocomplete({
	url: search_view,
  choiceSelector: 'a',
}).input.bind('selectChoice', function(e, choice, autocomplete) {
  setTimeout( function(){ window.location.href = choice.attr('href'); }, 500);
});