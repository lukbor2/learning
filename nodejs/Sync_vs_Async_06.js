//ASynchronous version of Example 05
/*
 * When countFiles is called it executes fs.readdir which returns the list of files in path
 * Then the callback of fs.readdir is executed and this callback calls the callback function passed
 * as an argument to countFiles (i.e. logCount).
 * Basically countFiles is NOT an asynchronous function, fs.readdir is!
 */


var fs = require('fs');

var path1 = "./",
path2 = ".././",
logCount;

function countFiles(path, callback) {
	fs.readdir(path, function (err, filenames) {
		callback(err, path, filenames.length);
	});
}

logCount = function (err, path, count) {
	console.log(count + " files in " + path);
};

countFiles(path1, logCount); 
countFiles(path2, logCount);