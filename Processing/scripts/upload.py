"""
Process runs
"""

import os, sys
import importlib
pathToUtilities = os.environ["HCALDQMUTILITIES"]
sys.path.append(pathToUtilities)

import Utils.Shell as Shell
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

#	this is the where processing starts
def process():
	""" processes runs """
	settings = importlib.import_module(sys.argv[1])
	logfile = open(settings.logfilename, "a")
	logfile.write("Started running at %s %s\n" % (Shell.gettimedate()))
	rdb = rundb.RunDB(settings, logfile); rdb.install()
	if locked(settings.lockpath): # return if the same process is running
		logfile.write("lock exists. Exiting...\n")
		return
	try:
		rdb.validate()
		filesToUpload = rdb.listFilesToUpload()
		for f in filesToUpload:
			logfile.write("filepath: "+f+"\n")
			
			try:
				cmd = "visDQMUpload %s %s" % (settings.hostname, f)
				logfile.write(cmd+"\n")
				o,e,rt = Shell.execute(cmd.split(" "))
				dir,filename = Shell.split(f)
				runType = rdb.runTypeByFileName(filename)
				runnumber = rdb.runNumberByFileName(filename)
				# skip runnumber 1 for now...
				if runnumber==1:
					continue
				logfile.write("runType: " + runType+"\n")
				logfile.write("OUTPUT Stream:\n"+o+"\n"+("-"*50)+"\n\n")
				logfile.write("ERROR Stream:\n"+e+"\n"+("-"*50)+'\n\n')
				if rt==0: # all is good
					rdb.mark(runnumber, runType, "uploaded")
					logfile.write("SUCCESS %d\n" % runnumber)
				else:
					rdb.mark(runnumber, runType, "uploadFailed")
					logfile.write("FAILED %d\n" % runnumber)
			except Exception as exc:
				logfile.write("Exception Name %s Exception Message %s\n" %
					(type(exc).__name__, str(exc.args)))
				rdb.mark(runnumber, runType.upper(), "failed")
				logfile.write("FAILED %d\n" % runnumber)
	except NameError as exc:
		logfile.write("NameErorr has occured. Exiting...\n")
		logfile.write("Error Message: "+str(exc.args)+'\n')
	except Exception as exc:
		logfile.write("Exception has been caught. Exiting... \n")
		logfile.write("ErrorName: %s ErrorMessage: %s\n" % (
			type(exc).__name__, str(exc.args)))
	finally:
		logfile.write("Finished running at %s %s\n" % (Shell.gettimedate()))
		Shell.rm(settings.lockpath)

if __name__=="__main__":
	process()
