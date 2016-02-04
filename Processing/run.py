"""
Launching script to process runs. Index them in the DB.
"""

import sys, os, glob
import settings
import RunDB
import RunInfoWrapper

def main():
	""" main entry point"""

	#	init
	ptype = sys.argv[1]
	db = RunDB(os.path.join(settings.dblocation, "RunDB"+ptype), ptype)
	riwrap = RunInfoWrapper()
	lfiles = os.listdir(settings.datapool)

	#	go thru all the files and process what's needed
	for filename in lfiles:
		runnumber = filename[settings.startpos:settings.endpos]
		runinfo = riwrap.getInfo(runnumber)
		run = LocalRun(runnumber, runInfo["NEVENTS"], runinfo["TIMESTAMP"],
			runinfo["CONFIG"])
		if db.exists(run):
			continue

		#	actual processing is here

	#	finalize
	db.finalize()

#
if __name__=="__main__":
	main()
