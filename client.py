import socket

class Client():
	def __init__(self, attributes):
		self.attributes = attributes

	def connect(self):
		self.tcpsoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print('created socket')
		if self.attributes['protocol'] == 'irc':
			try:
				self.tcpsoc.connect((self.attributes['server'], self.attributes['port']))
				print('connected')
			except:
				return False
		print(str(self.tcpsoc.recv(1024), 'ascii'), end="")
		print(str(self.tcpsoc.recv(1024), 'ascii'))
		print(str(self.tcpsoc.recv(1024), 'ascii'))
		self.tcpsoc.send(bytes('NICK '+self.attributes['nickname']+'\r\n', 'ascii'))
		self.tcpsoc.send(bytes('USER  '+self.attributes['username']+' 0 *  : '+self.attributes['realname']+'\r\n', 'ascii'))
		print(str(self.tcpsoc.recv(1024), 'ascii'))

	def disconnect(self):
		self.tcpsoc.close()

if __name__ == '__main__':
	setup = {
		'server':   '193.219.128.49',
		'port':     6667,
		'protocol': 'irc',
		'nickname': 'PythonChatClient',
		'username': 'jacobvalenta',
		'realname': 'Jacob Valenta',
	}
	client = Client(setup)
	client.connect()
	client.disconnect()
