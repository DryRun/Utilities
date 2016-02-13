"""
Processing Master Launcher
"""

import thread
import importlib

def child(msettings):
	pm2 = ProcessingMaster(1, msettings)
	pm2.start()

def start(msettings):
	msettings = importlib.import_module(argv[1])
	thread.start_new_thread(child, (msettings))
	pm1 = ProcessingMaster(0, msettings)
	pm1.start()

if __name__=="__main__":
	start()
