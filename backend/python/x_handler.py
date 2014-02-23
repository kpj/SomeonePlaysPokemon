import subprocess, time


def send_key_to_window(key, window_title):
	"""Writes given key to specified window
	"""

	# hacky because simply approach does not work...
	stdout, stderr = subprocess.Popen(
		[
			'xdotool',
			'search',
			window_title,
			'keydown', 
			'--clearmodifiers',  
			key
		], 
		stdout = subprocess.PIPE, 
		stderr = subprocess.PIPE
	).communicate()
	time.sleep(0.2)
	stdout, stderr = subprocess.Popen(
		[
			'xdotool',
			'search',
			window_title,
			'keyup', 
			'--clearmodifiers',  
			key
		], 
		stdout = subprocess.PIPE, 
		stderr = subprocess.PIPE
	).communicate()