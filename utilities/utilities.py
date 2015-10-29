"""
file:				utilities.py
author:				Viktor Khristenko
Description:
	A Set of Utility Functions/Classes
"""

#
#	Imports
#
import subprocess, os, sys

#	
#	File System Management
#
def mkdir(dirName):
	if not os.path.exists(dirName):
		cmd = "mkdir %s" % dirName
		subprocess.call(cmd, shell=True)

def cd(dirName):
	cmd = "cd %s" % dirName
	subprocess.call(cmd, shell=True)

def do(cmd):
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()
	return out

def getRunNumber(fileName):
	""" extract run number from DQM-like ROOT files """
	v = fileName.split('_')
	runNumber = v[len(v)-1].split('.')[0]
	runNumber = runNumber[len(runNumber)-6:]
	return int(runNumber)


