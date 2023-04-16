//Synchronous function

var fs = require('fs');

var path1 = "./",
path2 = ".././";

function countFiles(path) {
	var filenames = fs.readdirSync(path);
	return filenames.length;
}

console.log(countFiles(path1) + " files in " + path1);
console.log(countFiles(path2) + " files in " + path2);