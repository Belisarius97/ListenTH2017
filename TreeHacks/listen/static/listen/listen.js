const DEFAULT_DELAY = 10000;

function scrollTo(elemID) {
	var goto = $("#"+elemID)l
	$('html, body').animate({
		scrollTop: goto.offset().top
	}, DEFAULT_DELAY)
}