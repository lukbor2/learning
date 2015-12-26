// Synchronous function

var fs = require('fs');

function calculateByteSize() {
	var totalBytes = 0,
	i,
	filenames,
	stats;
	filenames = fs.readdirSync(".");
	for (i = 0; i < filenames.length; i ++) {
		stats = fs.statSync("./" + filenames[i]);
		totalBytes += stats.size;
	}
	console.log(totalBytes);
}

calculateByteSize();