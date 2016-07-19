"""
Server Class
"""


import sys,os
pathToUtilities = os.environ["HCALDQMUTILITIES"]
sys.path.append(pathToUtilities)

from XXX import XXX
from Communication.Socket import Socket
from Communication.ServerData import ServerData
import ServerCommands as cmds


class Server(XXX):
	def __init__(self, lid, msettings):
		XXX.__init__(self, lid)
		self.settings = msettings
		self.cmds = [self.cmd_work, self.cmd_stop, self.cmd_test]

	def initialize(self):
		self.ssocket = Socket()
		self.ssocket.bind(self.settings.hostname,self.settings.port)
		self.ssocket.listen(5)
		self.shouldStop = False

	def start(self):
		""" starts execution loop """
		while True:
			#	get the request
			c,a = self.ssocket.accept()
			print "Accepted connection from ",a
			pool = ""
			#	keep receiving until the end of message
			while True:
				msg = c.recv(self.settings.nbytes)
				if not msg: break
				pool+=msg

			#	Get the Server Message
			data = ServerData(pool)
			#	Dispatch quickly
			self.dispatch(c, a, data)
			if self.shouldStop:
				c.close()
				break
			c.close()
	
	def dispatch(self, connection, address, data):
		""" quickly dispatch """
		scmd,sdata = data.unpackPacket()
		try:
			self.cmds[int(scmd)](connection, address, sdata)
		except IndexError:
			print "Wrong Server Command: " + str(scmd)
	
	def finalize(self):
		print "Closing..."
		self.ssocket.close()

	#
	#	commands to be dispatched!
	#	each command gets connection, address and server specific data
	#
	def cmd_work(self, connection, address, data):
		""" To be reimplemented based on the type of the Server """
		return
	
	def cmd_stop(self, connection, address, data):
		self.shouldStop = True
		return

	def cmd_test(self, connection, address, data):
		print "Hello. This is just a Test"
		print "Data Transferred: ", data
		print "recceived data from: ", address
		return

#	testing
if __name__=="__main__":
	import importlib
	msettings = importlib.import_module(sys.argv[1])
	server = Server(0, msettings)
	server.initialize()
	try :
		server.start()
	except KeyboardInterrupt:
		server.finalize()
		sys.exit(0)
	server.finalize()
