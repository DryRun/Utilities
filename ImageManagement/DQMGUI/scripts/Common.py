"""
Common functions
"""

import re

template = "/(\w+)"

def match_path(path):
	nslash = path.count('/')
	rep = ""
	if nslash>0:
		for i in range(nslash):
			rep+=template
	r = re.match(rep, path)
	return r

def match_filename(filename, convention):
	if convention=="Offline":
		r = re.match("^DQM_V(\d+)_R(\d+)((__[-A-Za-z0-9_]+){3})\.root$",
			filename)
		return r
	elif convention=="Online":
		r = re.match("^DQM_V(\d+)(_[A-Za-z0-9]+)?_R(\d+)\.root$", filename)
		return r

subsystems = ["Hcal", "HcalCalib"]

if __name__=="__main__":
	r = match_filename("DQM_V0001_Hcal_R000266421.root", "Online")
	print r.groups()
