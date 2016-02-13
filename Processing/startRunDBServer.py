"""
RunDBServer Launcher
"""

import importlib
import sys

def start():
	msettings = importlib.import_module(sys.argv[1])
	dbs = RunDBServer(0, msettings)
	dbs.initialize()
	dbs.start()
	dbs.finalize()

if __name__=="__main__":
	start()




