"""
DB Wrapper
"""

import Utils.Shell

class Wrapper:
	def __init__(self, *argv):
		self.dbname = argv[0]
		self.qtemplate = argv[1]

	def query(self, *argv):
		""" query for what is specified. """
		runnumber = argv[0]
		selector = argv[1]
		selectorname = argv[2]

		cmd = "sqlplus -S %s@cms_rcms @%s %s %s %s" % (self.dbname, 
			self.qtemplate, selector, selectorname, runnumber)
		cmd = cmd.split(" ")
		o, e, rt = Shell.execute(cmd)

	def save(self, *argv):
		pass

if __name__=="__main__":
	import sys
	path = sys.argv[0]
	wrapper = Wrapper("cms_hcl_runinfo/run2009info", path)
	wrapper.query("264825", "STRING_VALUE", "NEVENTS")

