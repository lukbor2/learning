var fs = require('fs')
var path = require('path')

module.exports =  function (dir, filterStr, callback) {
	fs.readdir(dir, function (err, list) {
		if (err)
			return callback(err) //return is used so the code afterwards is NOT executed.
			
			list = list.filter(function (file) {
				return path.extname(file) === '.' + filterStr
			})
			callback(null, list) //If everything works, this function has now ended and calls the callback function (because everything is async
	})
}


