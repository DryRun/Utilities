"""
Run DB Server Class
"""

from Server import Server

class RunDBServer(Server):
	def __init__(self, lid, msettings):
		Server.__init__(self, lid, msettings)

	def initialize(self):
		Server.initialize(self)

	def work(self, cmddata):
		""" Reimplementfor Run DB Server here """
		print "Running Run DB Server"
		return

if __name__=="__main__":
	import importlib, sys
	msettings = importlib.import_module(sys.argv[1])
	rdbs = RunDBServer(0, msettings)
	rdbs.initialize()
	try:
		rdbs.start()
	except KeyboardInterrupt:
		rdbs.finalize()
		sys.exit(0)
	rdbs.finalize()
