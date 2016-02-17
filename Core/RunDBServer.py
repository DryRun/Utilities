"""
Run DB Server Class
"""

from Server import Server
import RunDB.RunDB as DB

class RunDBServer(Server):
	def __init__(self, lid, msettings):
		Server.__init__(self, lid, msettings)
		self.db = DB.RunDB(self.settings)

	def initialize(self):
		Server.initialize(self)
		self.db.initialize()

	def work(self, cmddata):
		""" Reimplementfor Run DB Server here """
		print "Running Run DB Server"
		return

	def finalize(self):
		Server.finalize(self)
		self.db.finalize()

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
