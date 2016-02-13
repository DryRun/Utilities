"""
Server Client to test the Servers functionality
"""

import importlib, sys, os
pathTohcaldqm = os.environ["HCALDQM"]
pathUtilities = pathToUtilities = pathTohcaldqm+"/"+"Utilities"
sys.path.append(pathToUtilities)


msettings = importlib.import_module(sys.argv[1])

data = [sys.argv[2], [1, 2, 3]]
import pickle
sdata = pickle.dumps(data)
from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect((msettings.hostname, msettings.port))

print "data to send: " ,sdata
s.send(sdata)

s.close()
