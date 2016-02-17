"""
DB Wrapper - generic Script to talk to WBM.
Works for RunInfo DB - enough as of 17Feb2016
"""

import os, sys
pathTohcaldqm = os.environ["HCALDQMSRC"]
pathToUtilities = pathTohcaldqm+"/"+"Utilities"
sys.path.append(pathToUtilities)

import Settings.Settings_Wrapper as SWrapper
import Utils.Shell as Shell

def runinfo_config2runtype(s):
	""" Convert the string you get from Run Info DB into the Run Type format"""
	s = s.split("/")
	s = s[len(s)-1]
	config = ""
	lasertypes = ["HBM", "HBP", "HEM", "HEP", "HO", "HF", "HPD"]
	#	NOTE: order matters for raddam - has to be in front of laser
	if "raddam" in s.lower():
		config = "raddam"
	elif "laser" in s.lower():
		config = "laser"
		for ltype in lasertypes:
			if ltype.lower() in s.lower():
				config+=ltype
	elif "pedestal" in s.lower():
		config = "pedestal"
	elif "led" in s.lower():
		config = "led"
	else:
		return None

	return config.upper()

class Wrapper:
	def __init__(self, *argv):
		self.dbname = argv[0]
		self.qtemplate = argv[1]
		self.logfileexists = False
		if len(argv)>2:
			#	file itself
			self.logfileexists = True
			self.logfile = argv[2]

	def query(self, *argv):
		""" query for what is specified. """
		runnumber = argv[0]
		quantity = argv[1]

		try:
			selector = SWrapper.quantitymap[quantity][0]
			selectorname = SWrapper.quantitymap[quantity][1]
		except KeyError as err:
			if self.logfileexists:
				self.logifle.write("Key Error Exception triggered\n")
				o = ""; e = ""; rt=100
				return o,e,rt

		#	build the query, then execute
		o = ""; rt=0; e=""
		try:
			cmd = "sqlplus -S %s@cms_rcms @%s %s %s %s" % (self.dbname, 
				self.qtemplate, selector, selectorname, runnumber)
			if self.logfileexists:
				self.logfile.write(cmd+"\n")
			cmd = cmd.split(" ")
			o, e, rt = Shell.execute(cmd)
		except Exception as exc:
			if self.logfileexists:
				self.logfile.write("Some Exception Triggered\n")
				return "","",100

		#	parse the output
		outLines = o.split('\n')
		return outLines[0],e,rt

	def save(self, *argv):
		pass

if __name__=="__main__":
	path = sys.argv[1]
	runnumber = sys.argv[2]
	quantity = sys.argv[3]
	wrapper = Wrapper("cms_hcl_runinfo/run2009info", path)
	x = wrapper.query(runnumber, quantity)
	print x
	print runinfo_config2runtype(x[0])
