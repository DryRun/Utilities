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
#	Some Variables
#

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

def execute(cmd):
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()
	return out,err, p.returncode


