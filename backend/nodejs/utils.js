// get MIME type from given filepath
function getMIMEType(path) {
	var end = path.split('.').pop();

	if(end == "html")
		return "text/html";
	else if(end == "js")
		return "text/javascript";
	else if(end == "css")
		return "text/css";
	else
		return "text/plain"
}

// create live stream and attach it to response object
function handle_process(res) {
	var width = -1;
	var height = -1;
	var top = 0;
	var left = 0;

	// get coordinates
	child_process.exec('xwininfo -root -tree', function(err, stdout, stderr) {
		if(err)
			return console.dir(err);

		var lines = stdout.toString().split("\n");
		for(var i = 0 ; i < lines.length ; i++) {
			if(lines[i].match(/vbam/)) {
				var r = /(\d+)x(\d+)\+(\d+)\+(\d+)\s+\+(\d+)\+(\d+)/;
				var m = lines[i].match(r);
				width = m[1];
				height = m[2];
				top = m[5];
				left = m[6];
				break;
			}
		}
		console.log(width, height, top, left);

		if(width == -1) {
			// vbam not running
			console.log("vbam not running");
			res.write('error');
		} else {
			// capture stream
			var ffmpeg = child_process.spawn(
				"ffmpeg",
				[
					"-re",
					"-f", "x11grab",
					"-r", "24",
					"-s", width + "x" + height,
					"-i", ":0+" + top + "," + left,
					"-g", "0",
					"-me_method", "zero",
					"-flags2", "fast",
					"-vcodec", "libvpx",
					"-preset", "ultrafast",
					"-tune", "zerolatency",
					"-b:v", "200k",
					"-crf", "40",
					"-f", "webm",
					"-"
				]
			);

			console.log("Redirected pipe...");
			ffmpeg.stdout.pipe(res);
		}
	});
}


// exports
exports.getMIMEType = getMIMEType;
exports.handle_process = handle_process;