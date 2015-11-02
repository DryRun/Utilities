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
	template = "query.sql"

	#	1. generate Run Info xml file
	dbWrapper = runInfo.RunInfoDWWrapper(runNumber, pathToSave, template)
	runtypestr = dbWrapper.generate()
	#	2. Process 
	cmd = "cmsRun %s/hcal_dqm_local_cfg.py inputFiles=file:%s runType=%s > %s" % (
		workDir, inputFile, runTypestr, logFile)
	cmd = cmd.split(" ")
	return utilities.do(cmd)

if __name__=="__main__":
	output,error = main()
	if error!=None:
		sys.exit(0)
		
	sys.exit(1)




