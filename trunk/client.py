#Pychat by Jacob Valenta
#Released under Creative Commons 0
#I dedicate this work to the public domain
from PIL import Image, Tkimage
from tkinter import *
import socket
import threading

class Client(Frame):
	def __init__(self, settings={}, master=None):
		Frame.__init__(self, master, background="white")
		self.grid()
		self.settings = settings
		self.buffer = bytearray()
		if self.settings == {}:
			self.displaySettings()
		self.master.title("Pychat v0.1")
		self.mainloop()

	def displaySettings(self):
		self.protocolInt = IntVar()

		self.background = Canvas(self, background="white", width=235, height=200, borderwidth=1, relief='flat')
		self.background.grid(row=0, column=0, columnspan=15, rowspan=20)

		self.optionIRC = Radiobutton(self, text="IRC", variable=self.protocolInt, background="white", activebackground="white", width=4, value=1)
		self.optionXMPP = Radiobutton(self, text="XMPP", variable=self.protocolInt, background="white", activebackground="white", width=4, value=2)
		self.optionIRC.grid(row=1, column=5, columnspan=4)
		self.optionXMPP.grid(row=1, column=9, columnspan=4)

		self.options = []
		for i in ['Protocol:', 'Username:', 'Real Name:', 'Server:', 'Port:', 'Channel:']:
			if i != 'Protocol:':
				self.options.append([
					Label(self, anchor=E, width=12, text=i, background="white"),
					Frame(self, background="BLACK", borderwidth=1, relief="sunken")
				])
				self.current = self.options[len(self.options)-1]
				self.current.append(
					Entry(self.current[1], relief="flat")
				)
			else:
				self.options.append(
					[Label(self, anchor=E, width=9, text=i, background="white")]
				)

		for i,c in enumerate(self.options):
			c[0].grid(row=2*i+1, column=0, columnspan=5)
			if i > 0:
				c[1].grid(row=2*i+1, column=6, columnspan=6)
				c[2].pack()

		self.quitbutton = Button(self, text="Quit", command=self.quit)
		self.quitbutton.grid(row=13, column=5, columnspan=2)

	def receiver(self):
		while True:
			self.buffer.extend(self.tcpsoc.recv(1024))
		
	def connect(self):
		self.tcpsoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print('created socket')
		if self.settings['protocol'] == 'irc':
			try:
				self.tcpsoc.connect((self.settings['server'], self.settings['port']))
				print('connected')
			except:
				return False
			print(str(self.tcpsoc.recv(1024), 'ascii'), end="")
			print(str(self.tcpsoc.recv(1024), 'ascii'))
			print(str(self.tcpsoc.recv(1024), 'ascii'))
			self.tcpsoc.send(bytes('NICK '+self.settings['nickname']+'\r\n', 'ascii'))
			self.tcpsoc.send(bytes('USER  '+self.settings['username']+' 0 *  : '+self.attributes['realname']+'\r\n', 'ascii'))
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
	client = Client()
