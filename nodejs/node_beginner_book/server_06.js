/* Now the server is able to identify the URL path which was requested
 * and it is able to call the appropriate handle for the requested URL
 */

var http = require("http");
var url = require("url");
function start(route, handle) {
	function onRequest(request, response) {
		var pathname = url.parse(request.url).pathname;
		console.log("Request for " + pathname + " received.");
		route(handle, pathname);
		response.writeHead(200, {"Content-Type": "text/plain"});
		response.write("Hello World");
		response.end();
	}
	http.createServer(onRequest).listen(8888);
	console.log("Server has started.");
}
exports.start = start;