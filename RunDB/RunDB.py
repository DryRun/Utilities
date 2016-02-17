"""
RunDB - API with the Run Database
"""

import sys, os
pathTohcaldqm = os.environ["HCALDQM"]
pathToUtilities = pathTohcaldqm+"/"+"Utilities"
sys.path.append(pathToUtilities)

from OnlineRun import OnlineRun
from OfflineRun import OfflineRun
from LocalRun import LocalRun
import shelve

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
		Config:
			LocalRun1: RunObject
			LocalRun2: RunObject

	"""
	def __init__(self, msettings):
		""" 
		dbname - pathname to the DB
		db is the pointer to the DB 
		"""
		self.settings = msettings
		self.__dbname = self.settings.dbname
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
		for ptype in self.settings.processingTypes:
			d = {}
			for x in self.settings.structure[ptype]:
				d[x.lower()] = {}
			self.__db[ptype.lower()] = d

	def checkptype(self, ptype, runobj):
		return (ptype.lower()==runobj.processingType().lower() or 
			runobj.processingType().lower() in ptype.lower())

	#
	#	Exist/Find functions by Run Object
	#	Assume you have complete object resolution
	#
	def find(self, ptype, runobj):
		""" object is returned, otherwise None"""
		#	get the branch
		if not self.checkptype(ptype, runobj):
			return None
		branch = self.__db[ptype]
		(x, run) = runobj.resolve()
		if x in branch.keys():
			if run in branch[x]:
				return branch[x][run]

		#	return None in the end
		return None

	def exists(self, ptype, runobj):
		"""  """
		return self.find(ptype, runobj)!=None

	#
	#	Content modifiers
	#
	def add(self, ptype, runobj):
		""" add the run object into the database. If already present,return"""
		if not self.checkptype(ptype, runobj):
			return
		#	do not add if exists
		if self.exists(ptype, runobj):
			return

		branch = self.__db[ptype]
		(x,run) = runobj.resolve()
		#	does such path exist in the DB
		if x not in branch.keys():
			branch[x.lower()] = {}
		branch[x][run] = runobj
		self.__db[ptype] = branch


	def delete(self, ptype, runobj):
		""" deletes the run object from the database if present """
		if not self.checkptype(ptype, runobj):
			return

		branch = self.__db[ptype]
		(x, run) = runobj.resolve()
		branch[x].pop(run)
		self.__db[ptype] = branch

	def update(self, ptype, runobj):
		""" 
		Update or replace the run. Assume it already exists
		Assume you don't modify the structure-based parameters
		"""
		branch = self.__db[ptype]
		(x, run) = runobj.resolve()
		branch[x][run] = runobj
		self.__db[ptype] = branch

	#
	#	Print Information
	#
	def printDB(self):
		""" Print the DB Structure """

		print "Printing Run DB"
		for ptype in self.__db.keys():
			branch = self.__db[ptype]
			s = "---"
			print s+"  "+ptype
			for x in branch.keys():
				print s*4 + "  " + x + ":"
				for run in branch[x].keys():
					print s*8+"  "+run

#
#	Testing
#
if __name__=="__main__":
	print "RunDB Hello"
	import importlib, sys
	msettings = importlib.import_module(sys.argv[1])
	db = RunDB(msettings)
	db.initialize()

	for i in range(10):
		r = LocalRun(i+10000, 100, "2015:01:01", "pedestal")
		db.add("local", r)
		r = OnlineRun(i+10000, 100, "2015:01:01", "physics")
		db.add("online-central", r)
		r = OfflineRun(i+10000, 100, "2015:01:01", "DATASET4")
		db.add("offline-central", r)
#	for i in range(10):
#		r = LocalRun(i, 100, "2015:01:01", "pedestal")
#		db.delete("local", r)
#		r = OnlineRun(i, 100, "2015:01:01", "physics")
#		db.delete("online-central", r)
#		r = OfflineRun(i, 100, "2015:01:01", "DATASET4")
#		db.delete("offline-central", r)

	run1 = LocalRun(1, 100, "2015:01:01", "laserhf")
	run2 = LocalRun(2, 100, "2015:01:01", "pedestal")
	run3 = LocalRun(3, 100, "2015:01:01", "laserhho")

	run4 = OfflineRun(1, 100, "2015:01:01", "DATASET1")
	run5 = OfflineRun(2, 100, "2015:01:01", "DATASET2")
	run6 = OfflineRun(3, 100, "2015:01:01", "DATASET3")

	db.printDB()

	db.finalize()

