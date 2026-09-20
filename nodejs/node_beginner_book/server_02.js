/* Still a simple http server, but in this example
 * the callback function is not anonymous (it is called onRequest).
 * Furthermore the command console.log("Server has started."); is executed immediately after
 * the createServer function has ended and before the onRequest is executed.
 * This is an example of how the asynchronous code works.
 */

var http = require("http");
function onRequest(request, response) {
	console.log("Request received.");
	response.writeHead(200, {"Content-Type": "text/plain"});
	response.write("Hello World");
	response.end();
}
http.createServer(onRequest).listen(8888);
console.log("Server has started.");