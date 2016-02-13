"""
Wrapper around sockets
"""

import socket

class Socket:
	def __init__(self, sock=None):
		if sock is None:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		else:
			self.sock = sock

	def bind(self, host, port):
		self.sock.bind((host, port))

	def listen(self, n):
		self.sock.listen(n)
	
	def accept(self):
		return self.sock.accept()

	def connect(self, host, port):
		self.sock.connect((host, port))

	def send(self, pmsg):
		self.sock.send(pmsg)

	def receive(self):
		return self.sock.recv(8192)

	def close(self):
		self.sock.close()
