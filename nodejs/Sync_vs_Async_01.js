// Synchronous function

var fs = require('fs'),
filenames,
i,
processId;

filenames = fs.readdirSync(".");
for (i = 0; i < filenames.length; i++) {
	console.log(filenames[i]);
}
console.log("Ready.");

processId = process.getuid();