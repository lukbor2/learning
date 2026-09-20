// ASynchronous version of Example 03

/*
 * Note how the First Callback is entirely executed
 * BEFORE the Second Callback is executed.
 * This is the principle of asynchronous programming
 */

var fs = require('fs');

var count = 0,
totalBytes = 0;

function calculateByteSize() {
	fs.readdir(".", function (err, filenames) {
		var i;
		count = filenames.length;
		
		for (i = 0; i < filenames.length; i++) {
			console.log("First Callback");
			fs.stat("./" + filenames[i], function (err, stats) {
				totalBytes += stats.size;
				console.log("Second Callback");
				count--;
				if (count === 0) {
					console.log(totalBytes);
				}
			});
		}
	});
}

calculateByteSize();