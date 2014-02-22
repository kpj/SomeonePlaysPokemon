import subprocess, time


"""Requires xdotool, xwininfo
"""


def get_window_id():
	"""Asks user to click on some window
	   returns window id
	"""

	p = subprocess.Popen('xwininfo', stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	stdout, stderr = p.communicate()

	win_id = stdout.decode(encoding='utf-8').split('\n')[5].split(' ')[3]
	return win_id

def send_key_to_window(key, window):
	"""Writes given key to specified window
	"""

	#cmd = ['xdotool', 'key', '--clearmodifiers', '--window', window, key]

	# hacky because simply approach does not work...
	stdout, stderr = subprocess.Popen(
		[
			'xdotool', 
			'keydown', 
			'--clearmodifiers', 
			'--window', 
			window, 
			key
		], 
		stdout = subprocess.PIPE, 
		stderr = subprocess.PIPE
	).communicate()
	time.sleep(0.2)
	stdout, stderr = subprocess.Popen(
		[
			'xdotool', 
			'keyup', 
			'--clearmodifiers', 
			'--window', 
			window, 
			key
		], 
		stdout = subprocess.PIPE, 
		stderr = subprocess.PIPE
	).communicate()

if __name__ == "__main__":
	i = get_window_id()
	send_key_to_window('d', i)