import json

from irc_bot import ChannelWrapper
import x_handler


# load config
config = json.load(open('config.json', 'r'))

# select window
print('Click on window to send keys to')
win_id = x_handler.get_window_id()

# glue components together
def glue(msg):
	print("Got %s, sending %s" % (msg, config['key_mapping'][msg]))
	x_handler.send_key_to_window(config['key_mapping'][msg], win_id)

# start channel analyser
chan = ChannelWrapper(config, glue)
chan.start()