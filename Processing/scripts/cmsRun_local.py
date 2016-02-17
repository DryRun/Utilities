#!/usr/bin/python

import sys, os, subprocess
import runInfo
import utilities

def main():
	#	input is quite redundant...
	inputFile = sys.argv[1]
	runNumber = sys.argv[2]
	workDir = sys.argv[3]
	pathToSave = workDir
	logFile = sys.argv[4]
	log = open(logFile, "w")
	template = "query.sql"

	#	for logging
	log.write(inputFile+'\n')
	log.write(runNumber+'\n')
	log.write(workDir+'\n')
	log.write(inputFile+'\n')
	log.write(template+'\n')

	#	1. generate Run Info xml file
	dbError = ""
	try:
		log.write("Initialize Run Info DB Wrapper\n")
		dbWrapper = runInfo.RunInfoDBWrapper(runNumber, pathToSave, template,
			log)
		runtypestr = dbWrapper.generate()
	except KeyError as err:
		log.write("Key Error Exception was triggered\n")
		runtypestr = "UNKNOWN"
		dbError = 'RunInfoDBError'

	#	2. Process 
	log.write("Process using CMSSW with RunType %s\n" % runtypestr)
	cmd = "cmsRun %s/hcal_dqm_local_cfg.py inputFiles=file:%s runType=%s" % (
		workDir, inputFile, runtypestr)
	log.write("Performing "+cmd+"\n")
	cmd = cmd.split(" ")
	output,error,rt = utilities.do(cmd)
	error = error + dbError
	
	log.write("###Starting Output\n"+output+'\n')
	log.write("###Starting Error\n"+error+"\n")

	return rt

if __name__=="__main__":
	er = main()
	if er==0:
		sys.exit(0)
	else:
		sys.exit(100)

	sys.exit(100)



