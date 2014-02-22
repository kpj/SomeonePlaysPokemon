import irc.client, irc.events
import threading, collections


class ChannelWrapper(object):
	def __init__(self, config, callback):
		self.reset_input_data()

		self.config = config
		self.callback = callback

	def start(self):
		"""Setup client, connect to server, ...
		"""

		# create client
		client = irc.client.IRC()

		# log into chat
#		server = client.server().connect(self.config['server'], self.config['port'], self.config['username'], self.config['oauth_password'])
		server = client.server().connect(self.config['server'], self.config['port'], self.config['username'])

		# add generic printing for everything
		f = lambda conn, event: 42#print(event.source, ' '.join(event.arguments))
		for val in irc.events.numeric.values():
			server.add_global_handler(val, f)

		# process chat messages
		server.remove_global_handler('pubmsg', f)
		server.add_global_handler('pubmsg', self.parse_input)

		# log into chat room
		server.join(self.config['channel'])

		# start analysis
		self.analyze_input()

		# wait
		client.process_forever()

	def reset_input_data(self):
		"""Clears chat-message cache
		"""
		self.input_data = collections.defaultdict(int)

	def parse_input(self, conn, event):
		"""Processes incoming chat messages
		   i.e. increases counter for valid ones
		"""
		sender = event.source
		msg = event.arguments[0]

		# update counter
		if msg in self.config['key_mapping'].keys():
			self.input_data[msg] += 1

	def analyze_input(self):
		"""Parses self.input_data and returns most prevalent entry
		"""

		inp = None
		# get max entry and use it
		if len(self.input_data) > 0:
			inp = max(self.input_data, key=(lambda key: self.input_data[key]))
		else:
			# No input received
			print('No input received')

		# clear input cache
		self.reset_input_data()

		# go into loop
		threading.Timer(1.0, self.analyze_input).start()

		if inp:
			self.callback(inp)


if __name__ == "__main__":
	import json


	config = json.load(open('config.json', 'r'))

	chan = ChannelWrapper(config, print)
	chan.start()
