#!/usr/bin/python

import sys, os, subprocess
import runInfo

def main():
	#	input is quite redundant...
	inputFile = sys.argv[1]
	runNumber = sys.argv[2]
	pathToSave = sys.argv[3]
	template = "query.sql"

	dbWrapper = runInfo.RunInfoDWWrapper(runNumber, pathToSave, template)
	dbWrapper.generate()

if __name__=="__main__":
	main()




