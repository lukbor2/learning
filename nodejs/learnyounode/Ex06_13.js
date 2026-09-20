/*
 * Here's my understanding of this exercise:
 * 
 * First of all, the function filterFn is an asynchronous function, meaning
 * it has been build to behave like an async function.
 * 
 * Second, the function called in the main module (i.e. filterFn) is defined in the
 * auxiliary module (Ex06_13_module.js); BUT the callback function called after filterFn has finished
 * is defined HERE, in the main module. This can be a little confusing.  What I mean is in Ex06_13_module.js 
 * we do not say what the callback function does, what the callback function does is defined here.
 * 
 * Keeping these 2 things in mind, the code becomes clear.
 * 
 * Basically filterFn is called, so the code defined in Ex06_13_module.js is executed passing the 3 arguments.
 * That code executes first fs.readdir, if fs.readdir has an error then filterFn.myfunc ends and returns callback(err)
 * which means the anonymous function implemented here is executed passing err as an argument. And looking at the implementation
 * it means the error message is printed to the console.
 * If fs.readdir is successful then the callback function is called with err and list as arguments, which means
 * the anonymous function implemented here is executed passing err and list as arguments. And looking at the implementation 
 * it means the list of files is printed to the console.
 * 
 */


var filterFn = require('./Ex06_13_module.js');

var dir = process.argv[2];
var filterStr = process.argv[3];

filterFn(dir, filterStr, function (err, list) {
	if (err)
		return console.error('There was an error:', err)
		list.forEach(function (file) {
			console.log(file)
		})
})