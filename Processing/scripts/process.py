"""
Process runs
"""

import os, sys
import importlib
pathToUtilities = os.environ["HCALDQMUTILITIES"]
sys.path.append(pathToUtilities)

import Utils.Shell as Shell
import WBM.Wrapper as wbm
import RunDB.RunDB_OLD as rundb
import Processing.scripts.run_AnalysisTrend as run

def locked(lockpath):
	if Shell.exists(lockpath):
		return True

	Shell.touch(lockpath)
	return False

#	this should be redone based on the input name
#	for local runs it's 4to10 
def runNumber(filename):
	return int(filename[4:10])

def getRunType(wbmdb, runnumber, settings):
	o,e,rt = wbmdb.query(runnumber, "CONFIG_NEW")
	if o=="":
		o,e,rt = wbmdb.query(runnumber, "CONFIG_OLD")
	if rt>0 or e!="" or o=="":
		return None

	# if all went good - return the type
	return wbm.runinfo_config2runtype(o)

#	this is the where processing starts
def process():
	""" processes runs """
	settings = importlib.import_module(argv[1])
	logfile = open(settings.logfilename, "w")
	logfile.write("Started running at %s %s\n" % (Shell.gettimedata()))

	if locked(settings.lockpath): # return if the same process is running
		return

	wbmdb = wbm.Wrapper(settings.runinfo_db_name,
		settings.runinfo_db_querytemplate, logfile)
	runlist = Shell.ls_glob(settings.poolsource)
	for f in runlist:
		runnumber = runNumber(Shell.split(f)[1])
		filesize = Shell.getsize(f)
		if filesize>settings.filesizelimit:
			continue

		#	if this guy is already present in the db
		#	go to the next guy
		if db.exists(runnumber):
			continue
		else:
			#	doesn't exist yet
			runType = getRunType(db, runnumber, settings)
			if runType==None:
				continue

			#	mark and process
			db.mark(runnumber, runType.upper(), "processing")
			try:
				listLastRuns,listLastRunFiles = db.getLast(runType.upper())
			except IndexError as exc:
				continue
			rt = run.run(settings.cmssw_config, f, runType.upper(), 
				settings.cmssw_harvesterconfig, listLastRuns,
				listLastRunFiles, logfile)	
			if rt==0: # all is good
				db.mark(runnumber, runType.upper(), "processed")
				logfile.write("SUCCESS %d" % runnumber)
			else:
				db.mark(runnumber, runType.upper(), "failed")
				logfile.write("FAILED %d" % runnumber)

if __name__=="__main__":
	process()
