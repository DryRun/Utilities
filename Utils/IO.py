"""
IO Utilities
"""

import sys,os
pathToUtilities = os.environ["HCALDQMUTILITIES"]
sys.path.append(pathToUtilities)

def getRunNumber(filename):
	return int(filename[len(filename)-11:len(filename)-5])
