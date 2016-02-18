"""
Old Run DB wrapper
"""

import sys, os
pathToUtilities = os.environ["HCALDQMUTILITIES"]
sys.path.append(pathToUtilities)

import Utils.Shell as Shell

class RunDB:
	def __init__(self, msettings):
		self.settings = msettings
	
	def install(self):
		""" install the DB-like structure. Assume dbpool exists """
		if Shell.exists(Shell.join(sef.settings.dbpool, 
			self.settings.processingtype)):
			return
		else:
			self.installStructure()

	def installStructure(self):
		#	build top directory of db for the specified ptype
		Shell.mkdir(Shell.join(self.settings.dbpool, 
			self.settings.processingtype.upper()))
		if self.settings.processtype.upper()=="LOCAL":
			for runtype in self.settings.runtypes:
				Shell.mkdir(Shell.join(self.settings.dbpool, 
					self.settings.processingtype.upper()+"/"+runtype.upper()))
		else:
			pass


	def exists(self, runnumber):
		dbpool = self.settings.dbpool
		if self.settings.processingtype.upper()=="LOCAL":
			ptype = "LOCAL"
			for runtype in self.settings.runtypes:
				if Shell.exists(Shell.join(dbpool, 
					ptype+"/"+runType.upper()+"/"+str(runnumber))):
					return True
		else:
			return False

		return False

	def mark(self, runnumber, runType, m):
		dbpool = self.settings.dbpool
		ptype = self.settings.processingtype.upper()
		if Shell.exists(Shell.join(dbpool, ptype+"/"+runType.upper()+"/"+
			str(runnumber))):
			#	new run number - create a folder for it
			Shell.mkdir(Shell.join(dbpool, ptype+"/"+runType.upper()+"/"+
				str(runnumber)))
		#	touch a mark
			Shell.touch(Shell.join(dbpool, ptype+"/"+runType.upper()+"/"+
				str(runnumber)+"/"+m))

	def getLast(self, runType):
		""" list the last N runfiles and runnumbers for runType """
		lfiles = []
		lruns = []
		dbpool = self.settings.dbpool
		ptype = self.settings.processingtype.upper()
		dqmiopool = self.settings.dqmiopool

		if ptype=="LOCAL":
			runpathlist = Shell.ls_glob(Shell.join(dbpool, ptype+"/"
				+runType.upper()+"/*"))
			for runpath in runpathlist:
				runpath = runpath.split("/")
				lruns[len(lruns):] = [int(runpath[len(runpath)-1])]
			for run in lruns:
				runfileslist = Shell.ls_glob(Shell.join(dbpool, 
					ptype+"/*%d*%s*%s*" % (run, runType.uppper(), 
					self.settings.localrunlabel)))
				if len(runfileslist)==0 or len(runfileslist)>1:
					raise IndexError(runfileslist, run)
				lfiles[len(lfiles)] = runfileslist
			
		# return last n runs,files
		return (lruns[-self.settings.numrunsForTrend:],
			lfiles[-self.settings.numrunsForTrend:])

if __name__=="__main__":

