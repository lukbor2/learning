/*
 * This version of requestHandlers.js is not great. Because if a request for start() arrives first
 * and then a request for upload() arrives, the request for upload must wait the 10 seconds of the sleep function
 * in start().
 * That is because - I think - nodejs runs ONE PROCESS for ALL requests; in this implementation start() and upload()
 * are both synchronous, therefore we must wait for start() to end before processing upload().
 */

function start() {
	console.log("Request handler 'start' was called.");
	
	function sleep(milliSeconds) {
		var startTime = new Date().getTime();
		while (new Date().getTime() < startTime + milliSeconds);
	}
	
	sleep(10000);
	return "Hello Start";
}
function upload() {
	console.log("Request handler 'upload' was called.");
	return "Hello Upload";
}
exports.start = start;
exports.upload = upload;