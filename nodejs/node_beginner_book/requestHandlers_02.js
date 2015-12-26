/*
 * In this case, the asynchronous exec function is used. But still it does not work
 * because the variable content is returned immediately before the exec function has finished
 * so when content is return it holds "empty" and not the list of files given by ls -lah.
 */

var exec = require("child_process").exec;

function start() {
	console.log("Request handler 'start' was called.");
	
	var content = "empty";
	
	exec("ls -lah", function (error, stdout, stderr) {
		content = stdout;
	});
	
	return content;
}

function upload() {
	console.log("Request handler 'upload' was called.");
	return "Hello Upload";
}

exports.start = start;
exports.upload = upload;