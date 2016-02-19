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
import subprocess, glob, time

#	
#	File System Management
#
def mkdir(dirName):
	if not os.path.exists(dirName):
		cmd = "mkdir %s" % dirName
		subprocess.call(cmd, shell=True)

def rm(pathfile):
	cmd = "rm %s" % pathfile
	subprocess.call(cmd, shell=True)

def rmdir(pathdir):
	cmd = "rm -rf %s" % pathdir
	subprocess.call(cmd, shell=True)

def touch(pathfile):
	if not os.path.exists(pathfile):
		cmd = "touch %s" % pathfile
		subprocess.call(cmd, shell=True)

def call(cmd):
	subprocess.call(cmd, shell=True)

def exists(path):
	return os.path.exists(path)

def getsize(path):
	return os.path.getsize(path)

def fork():
	return os.fork()

def gettimedate():
	""" return (time, data) """
	return time.strftime("%X"),time.strftime("%x")

def cd(dirName):
	os.chdir(dirName)

def ls_glob(pathpattern):
	return glob.glob(pathpattern)

def ls_os(path):
	return os.listdir(path)

def split(pathfile):
	return os.path.split(pathfile)

def join(path, filename):
	return os.path.join(path, filename)

def execute(cmd):
	out="";err="";rt=100
	try:
		p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = p.communicate()
		rt = p.returncode
		return out,err, rt
	except Exception as exc:
		print exc.args
		print out,err
	finally:
		return out,err,rt

if __name__=="__main__":
	print join("/data/hcaldqm/HCALDQM/Utilities/Processing/scripts", "process.sh")
