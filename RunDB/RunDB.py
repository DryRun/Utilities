
#
#	RunDB - Manager over the Run Database
#

from OnlineRun import OnlineRun
from OfflineRun import OfflineRun
from LocalRun import LocalRun

import shelve
import RunDBSettings as settings

class RunDB:
	"""
	Run Database class - interface to the shelve of runs.
	Structure is organized in terms of processing types, datasets, streams,
	run numbers, configuration, etc... Structure:
	Online:
		Physics stream:
			OnlineRun1:
				Run Object
			OnlineRun2:
				Run Object
		Calib stream:
			...
	Offline:
		PD1:
			OfflineRun1:
				RunObject
			OfflineRun2:
				RunObject
		PD2:
			...
		PD3:
			...
	Local:
		Config:
			LocalRun1:
				RunObject
			LocalRun2:
				RunObject

	NOTE: Curruntly use 1 processing type per DB
	"""
	def __init__(self, dbname, processingtype):
		self.__dbname = dbname
		self.__ptype = processingtype
		self.__db = None

	#
	#	Init, finalize, Structure definitions
	#
	def initialize(self):
		""" Open the DB """
		self.__db = shelve.open(self.__dbname)
		if len(self.__db.keys())==0:
			self.createDBStructure()

	def finalize(self):
		""" Close """
		self.__db.close()

	def createDBStructure(self):
		""" 
		This is done only once - generates overall structure of the DB.
		However, new Datasets could be added, new configurations...
		or new processing types
		"""
		d = {}
		for x in settings.structure[self.__ptype]:
			d[x] = {}
		self.__db[self.__ptype] = d

	#
	#	Exist/Find functions
	#
	def find(self, runobj):
		""" object is returned, otherwise None"""
		db = self.__db[self.__ptype]
		#	if this configuration, dataset or stream exists
		s = self.secondlvl(runobj)
		if s in db.keys():
			#	if such run number exists
			if runobj.run() in db[s].keys():
				return db[s][runobj.run()]

		return None

	def exists(self, runobj):
		"""  """
		return self.find(runobj)!=None

	#
	#	Content modifiers
	#
	def addRun(self, runobj):
		""" add the run object into the database. If already present,return"""
		if self.exists(runobj):
			return

		if runobj.processingType()!=self.__ptype:
			print "Trying to add wrong processing type"
			return

		if runobj.processingType()=="Online":
			self.addOnline(runobj)
		elif runobj.processingType()=="Offline":
			self.addOffline(runobj)
		elif runobj.processingType()=="Local":
			self.addLocal(runobj)
		else:
			print "Unknown Processing Type - Corruption"
			return

	def deleteRun(self, runobj):
		""" deletes the run object from the database if present """
		if not self.exists(runobj):
			return

		if not self.validPType(runobj):
			print "Invalid processing type"
			return

		if self.__ptype=="Online":
			self.deleteOnline(runobj)
		elif self.__ptype=="Offline":
			self.deleteOffline(runobj)
		elif self.__ptype=="Local":
			self.deleteLocal(runobj)
		else:
			print "Unknown processing type - Corruption"
			return

	def updateRun(self, runobj):
		""" 
		Update or replace the run. No check for existence.
		Assume you don't modify the structure-based parameters
		"""
		if not self.validPType(runobj):
			print "Invalid processing type"
			return

		if self.__ptype=="Online":
			self.addOnline(runobj)
		elif self.__ptype=="Offline":
			self.addOffline(runobj)
		elif self.__ptype=="Local":
			self.addLocal(runobj)
		else:
			print "Unknown processing type - Corruption"
			return
	
	def addOnline(self, runobj):
		onlineruns = self.__db["Online"]
		if runobj.stream() not in onlineruns.keys():
			onlineruns[runobj.stream()] = {}
		onlineruns[runobj.stream()][runobj.run()] = runobj
		self.__db["Online"] = onlineruns

	def addOffline(self, runobj):
		offlineruns = self.__db["Offline"]
		if runobj.dataset() not in offlineruns.keys():
			offlineruns[runobj.dataset()]={}
		offlineruns[runobj.dataset()][runobj.run()] = runobj
		self.__db["Offline"] = offlineruns

	def addLocal(self, runobj):
		localruns = self.__db["Local"]
		if runobj.configuration() not in localruns.keys():
			localruns[runobj.configurarion]={}
		localruns[runobj.configuration()][runobj.run()] = runobj
		self.__db["Local"] = localruns

	def deleteOnline(self, runobj):
		onlineruns = self.__db["Online"]
		onlineruns[self.secondlvl(runobj)].pop(runobj.run())
		self.__db["Online"] = onlineruns
	
	def deleteOffline(self, runobj):
		offlineruns = self.__db["Offline"]
		offlineruns[self.secondlvl(runobj)].pop(runobj.run())
		self.__db["Offline"] = offlineruns

	def deleteLocal(self, runobj):
		localruns = self.__db["Local"]
		localruns[self.secondlvl(runobj)].pop(runobj.run())
		self.__db["Local"] = localruns

	#
	#	Print Information
	#
	def printDB(self):
		""" Print the DB Structure """
		for ptype in self.__db.keys():
			print ptype
			print self.__db[ptype]

	#
	#	Helpful functions
	#
	def secondlvl(self, runobj):
		"""
		as our DB has 3-level structure, get 2nd level
		"""
		db = self.__db[self.__ptype]
		if self.__ptype=="Online":
			return runobj.stream()
		elif self.__ptype=="Offline":
			return runobj.dataset()
		elif self.__ptype=="Local":
			return runobj.configuration()
		return "None"

	def validPType(self, runobj):
		return self.__ptype==runobj.processingType()

#
#	Testing
#
if __name__=="__main__":
	print "RunDB Hello"
	dbOnline = RunDB("RunDBOnline", "Online")
	dbOnline.initialize()
	dbOnline.printDB()

	dbOnline.finalize()
	dbOffline = RunDB("RunDBOffline", "Offline")
	dbOffline.initialize()
	dbOffline.printDB()

	run1 = OfflineRun(1111, 100, "2015:01:01", "NEWDATASET")
	run2 = OfflineRun(1111, 100, "2015:01:01", "DATASET2")
	run3 = OfflineRun(1111, 100, "2015:01:01", "DATASET3")
	run4 = OfflineRun(1111, 100, "2015:01:01", "DATASET4")
	run5 = OfflineRun(255535, 100000, "2016:01:01", "MINBIAS")
	run6 = OfflineRun(255600, 100000, "2016:01:01", "MINBIAS")
	dbOffline.addRun(run1)
	dbOffline.addRun(run2)
	dbOffline.addRun(run3)
	dbOffline.addRun(run4)
	dbOffline.addRun(run5)
	dbOffline.addRun(run6)

	dbOffline.deleteRun(run2)

	dbOffline.printDB()

	dbOffline.finalize()


