"""
Server Class
"""


import sys,os
pathTohcaldqm = os.environ["HCALDQMSRC"]
pathToUtilities = pathTohcaldqm+"/"+"Utilities"
sys.path.append(pathToUtilities)

from XXX import XXX
from Communication.Socket import Socket
from Communication.ServerData import ServerData
import ServerCommands as cmds


class Server(XXX):
	def __init__(self, lid, msettings):
		XXX.__init__(self, lid)
		self.settings = msettings
		self.cmds = [self.work, self.stop, self.test]

	def initialize(self):
		self.ssocket = Socket()
		self.ssocket.bind(self.settings.hostname,self.settings.port)
		self.ssocket.listen(5)
		self.shouldStop = False

	def start(self):
		while True:
			c,a = self.ssocket.accept()
			print "Accepted connection from ",a
			cmddata = c.recv(self.settings.nbytes)
			if not cmddata: break
			#	1. initialize Data class
			data = ServerData(cmddata)
			self.dispatch(c, a, data)
			if self.shouldStop:
				c.close()
				break
			c.close()
	
	def dispatch(self, connection, address, data):
		""" data = Data.Data object"""
		icmd,sdata = data.unpackPacket()
		try:
			self.cmds[int(icmd)](sdata)
		except IndexError:
			print "Wrong Server Command: " + str(icmd)

	def work(self, data):
		""" To be reimplemented based on the type of the Server """
		return
	
	def stop(self, data):
		self.shouldStop = True
		return

	def test(self, data):
		print "Hello. This is just a Test"
		print "Data Transferred: ", data
		return

	def finalize(self):
		print "Closing"
		self.ssocket.close()

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
