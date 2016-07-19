"""
Launching Server - launches execution processes which actually do the 
processing/analysis
"""

from Server import Server

class LaunchingServer(Server):
	def __init__(self, lid, mseetings):
		Server.__init__(self, lid, msettings)

	def intialize(self):
		Server.initialize(self)

	def cmd_work(self ,cmddata):
		""" Reimplement """
		print "Running Launching Server"

	def finalize(self):
		Server.finalize(self)

if __name__=="__main__":
	import importlib, sys
	msettings = importlib.import_module(sys.argv[1])
	lserver = LaunchingServer(0, msettings)
	lserver.initialize()
	try:
		lserver.start()
	except KeyboardInterrupt:
		lserver.finalize()
		sys.exit(0)
	lserver.finalize()
