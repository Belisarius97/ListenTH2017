const DEFAULT_DELAY = 1000;

/*
$('a[href^="#"]').on('click', function(event) {
    var target = $(this.getAttribute('href'));
    if( target.length ) {
        event.preventDefault();
        $('html, body').stop().animate({
            scrollTop: target.offset().top
        }, DEFAULT_DELAY);
    }
});
*/

$(document).ready(function(){
	//$('a[href^="#"]').bind('click.smoothscroll',function (e) {
	$('a[href="#langSelect"]').bind('click.smoothscroll',function (e) {
	    e.preventDefault();
	 
	    var target = this.hash,
	    $target = $(target);
	 
	    $('html, body').stop().animate({
	        'scrollTop': $target.offset().top
	    }, DEFAULT_DELAY, 'swing', function () {
	        window.location.hash = target;
	    });
	});
});
/*
$(function(){
	
	$('.menu').click(function(e) {
		$('html').toggleClass('menu-active');
		e.preventDefault();
	});
	
	$('.menu-wrapper a').click(function(e) {
		$('html').removeClass('menu-active');
	});
	
	$('.menu-close').click(function(e) {
		$('html').removeClass('menu-active');
	});
});*/