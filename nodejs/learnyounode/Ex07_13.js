var http = require('http');
var urlget = process.argv[2]; // the argument passed to the command line is the URL I will use for the get

//console.log("URL: " + urlget);

http.get(urlget, function(response){
	response.setEncoding('utf8');
		response.on("data", function(data) {
		console.log(data);
	})
	
	// response.on('data', console.log); I could have used this instead of the anonymous function which logs the data after response.on
	
	response.on('error', console.error);
}
)