var fs = require('fs');
var buf = fs.readFileSync(process.argv[2]);
var str = buf.toString();
var arr = str.split('\n');
console.log(arr.length-1); //the last line does not end with new line and we want to count new lines

// remember to run it like this
// node Ex03_13.js /home/luca/Documents/learning/nodejs/testfile
