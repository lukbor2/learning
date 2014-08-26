var fs = require('fs');
// this is an example of a callback
fs.readFile(process.argv[2],'utf8', function(err, buf){
	if(err){
		console.log(err);
		return;
		}
	var arr = buf.split('\n');
	console.log(arr.length-1); //the last line does not end with new line and we want to count new lines
	}
)



