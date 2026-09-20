// ASynchronous version of Example 01

/*
 * Callback functions are the basic building block of asynchronous event-driven programming in Node.js.
 * They are functions passed as an argument to an asynchronous I/O operation.
 * They are called once the operation is finished. 
 */


var fs = require('fs'),
processId;

fs.readdir(".", function (err, filenames) {
	var i;
	for (i = 0; i < filenames.length; i++) {
		console.log(filenames[i]);
	}
	console.log("Ready.");
});

processId = process.getuid();

