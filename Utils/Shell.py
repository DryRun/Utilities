"""
file:				utilities.py
author:				Viktor Khristenko
Description:
	A Set of Utility Functions/Classes
"""

import sys, os
pathTohcaldqm = os.environ["HCALDQMSRC"]
pathToUtilities = pathTohcaldqm+"/"+"Utilities"
sys.path.append(pathToUtilities)

#
#	Imports
#
import subprocess, glob

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

def ls_glob(pathpattern):
	return glob.glob(pathpattern)

def ls_os(path):
	return os.listdir(path)

def split(pathfile):
	return os.path.split(pathfile)

def join(path, filename):
	return os.path.join(path, filename)

def execute(cmd):
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()
	return out,err, p.returncode

if __name__=="__main__":
	print join("/data/hcaldqm/HCALDQM/Utilities/Processing/scripts", "process.sh")
