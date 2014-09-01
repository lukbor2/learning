//Now the server is part of a module which can be used elsewhere, for example in index.js

var http = require("http");
function start() {
	function onRequest(request, response) {
		console.log("Request received.");
		response.writeHead(200, {"Content-Type": "text/plain"});
		response.write("Hello World");
		response.end();
	}
	http.createServer(onRequest).listen(8888);
	console.log("Server has started.");
}
exports.start = start;