import socket

class Client():
	def __init__(self, serverIp="193.219.128.49", serverPort=6667, clientType="irc"):
		self.status = "initializing"
		if clientType == "irc":
			self.clientType = "irc"
			self.serverIp = serverIp
			self.serverPort = serverPort
			self.initIRC()

	def initXMPP(self):
		#TODO
		pass

	def initIRC(self):
		self.status = "connecting"
		self.tcpsoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			self.tcpsoc.connect((self.serverIp, self.serverPort))
			self.tcpsoc.recv(1024)
			self.tcpsoc.recv(1024)
		except:
			print('Could not establish a connection with the server at this time')
			return False

	def IRC(self):
		pass

	def quit(self):
		self.tcpsoc.close()

if __name__ == '__main__':
	client = Client()
