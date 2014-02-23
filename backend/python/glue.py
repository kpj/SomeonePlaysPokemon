import json

from irc_bot import ChannelWrapper
import x_handler


# load config
config = json.load(open('config.json', 'r'))

# glue components together
def glue(msg):
	print("Got %s, sending %s" % (msg, config['irc']['key_mapping'][msg]))
	x_handler.send_key_to_window(config['irc']['key_mapping'][msg], win_id)

# start channel analyser
chan = ChannelWrapper(config['irc'], glue)
chan.start()