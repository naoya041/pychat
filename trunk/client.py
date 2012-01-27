import socket

class Client():
	def __init__(self, serverIp="193.219.128.49", serverPort=6667, clientType="irc"):
		if clientType == "irc":
			self.clientType = "irc"
			self.serverIp = serverIp
			self.serverPort = serverPort
			self.initIrc()

	def initXmpp(self):
		pass

	def initIrc(self):
		self.tcpsoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.tcpsoc.connect((self.serverIp, self.serverPort))
		self.tcpsoc.close()

if __name__ == '__main__':
	client = Client()
