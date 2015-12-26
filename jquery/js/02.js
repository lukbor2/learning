// This is the custom JavaScript file referenced by index.html. You will notice
// that this file is currently empty. By adding code to this empty file and
// then viewing index.html in a browser, you can experiment with the example
// page or follow along with the examples in the book.
//
// See README.txt for more information.

$(document).ready(function() {
	$('#selected-plays > li').addClass('horizontal');
	$('#selected-plays li:not(.horizontal)').addClass('sub-level');
	$('a[href^="mailto:"]').addClass('mailto');
	$('a[href$=".pdf"]').addClass('pdflink');
	$('a[href^="http"][href*="henry"]').addClass('henrylink');
	$('tr:nth-child(odd)').addClass('alt');
	// $('td:contains(Henry)').addClass('highlight');
	$('td:contains(Henry)').nextAll().addBack().addClass('highlight');
	$('a').filter(function() {
		return this.hostname && this.hostname != location.hostname;
		}).addClass('external');
	
	//Chapter 2 - Ex 01: Add a class of special to all of the <li> elements at the second level of the nested list.
	$('li.horizontal').find('li').addClass('special');
	
	//Chapter 2 - Ex 02: Add a class of year to all the table cells in the third column of a table.
	$('td:nth-child(3)').addClass('year');
		
	//Another solution for the same exercise
		//$('tr').find('td:eq(2)').addClass('year');
	
	//Chapter 2 - Ex 03: Add the class special to the first table row that has the word Tragedy in it.
	$('tr').children(':contains(Tragedy)').first().addClass('special');
	$('tr').children(':contains(Tragedy)').first().siblings().addClass('special');
	
	// Chapter 2 - Ex 04: Select all of the list items (<li>s) containing a link (<a>). Add the
	// class afterlink to the sibling list items that follow the ones selected.
	
	$('li').has('a').nextAll().addClass('afterlink');
	
	//Chapter 2 - Ex 05: Add the class tragedy to the closest ancestor <ul> of any .pdf link
	
	
});