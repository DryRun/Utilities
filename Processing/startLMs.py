"""
Launcher Master Launcher - tautology
"""

import thread

def child(msettings):
	lm2 = LaunchingMaster(1, msettings)
	lm2.start()

def start():
	msettings = importlib.import_module(argv[1])
	thread.start_new_thread(child, (msettings))
	lm1 = LaunchingMaster(0, msettings)
	lm1.start()

if __name__=="__main__":
	start()
