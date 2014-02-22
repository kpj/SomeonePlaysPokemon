var http = require('http')
	child_process = require('child_process'),
	fs = require('fs');

var utils = require('./utils');
var config = require('./../../config.json')['stream'];


http.createServer(function (req, res) {
	var path = req.url;
	if(path == '/video.webm') {
		utils.handle_process(res);
	} else {
		if(path == "/") path = "/index.html";

		try {
			res.writeHead(200, {'Content-Type': utils.getMIMEType(path)});
			res.end(fs.readFileSync('./frontend/' + path));
		} catch(err) {
			console.log(err);

			res.writeHead(404, {'Content-Type': 'text/plain'});
			res.end('Sorry :-/');
		}
	}
}).listen(config['port']);