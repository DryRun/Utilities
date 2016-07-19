#!/usr/bin/python

import os, time, sys
from multiprocessing import Process, Lock, Array
import getopt

pathToUtilities = os.environ["HCALDQMUTILITIES"]
pathToHCALDQM = os.environ["HCALDQM"]
pathToLogs = os.environ["HCALDQMLOGS"]
sys.path.append(pathToUtilities)

import Utils.Shell as Shell

configList = [
	"hcal_dqm_sourceclient-live_cfg_noupload.py", 
	"hcal2_dqm_sourceclient-live_cfg_noupload.py",
	"hcal3_dqm_sourceclient-live_cfg_noupload.py",
	"hcal4_dqm_sourceclient-live_cfg_noupload.py"]
subsystemnames = ["Hcal", "Hcal2", "Hcal2", "Hcal"]

def process(id, runnumber, lock, states, configid):
	msg = "Processing cmssw... pid=%d  Run=%s"
	with lock:
		print (msg % (os.getpid(), runnumber))
	
		cmd = "%s/Processing/scripts/run_online.sh %s %s" % (pathToUtilities,
			runnumber, configList[configid])
		print cmd
		o,e,r = Shell.execute(cmd.split(" "))
#		o,e,r = ("", "", 0)
		f = open(pathToLogs+"/log.process.%s.%d" % (runnumber, configid), 'w')
		f.write("Output:\n%s" % o)
		f.write("Error:\n%s" % e)
		f.close()
		states[id] = 1

def upload(runnumber, configid):
	msg = "Uploading to DQM GUI... Run=%s" % runnumber
	cmd = "%s/upload.sh 8070 online-dev %s/DQM_V0001_%s_R000%s.root" % (
		pathToHCALDQM+"/GUI", pathToHCALDQM+"/DQMIO/ONLINE_PLAYBACK", 
		subsystemnames[configid], runnumber)
	print cmd
	o,e,r = Shell.execute(cmd.split(" "))
	f = open(pathToLogs+"/log.upload.%s" % runnumber, "w")
	f.write("Ouput:\n%s" % o)
	f.write("Error:\n%s" % e)
	f.close()
	return

def validateInput(runlist, configid):
	for l in runlist:
		try:
			x = int(l)
		except ValueError:
			return False
	try:
		int(configid)
	except ValueError:
		return False
	return True

def main(argv):
	#	get list of runs to process
	try:
		opts , args = getopt.getopt(argv, "hr:c:", ["help=", "runlist=", "config="])
	except getopt.GetoptError:
		print './process_replay.py -r <csv runlist> -c <config>'
		print "config types: 0, 1"
		print "0 - raw + digi + tps"
		print "1 - utca vs vme + reco"
		print "2 - utca vs vme only"
		print "3 - raw + digi + tps + qie10"
		sys.exit(2)
	config = 0
	runlist = []
	for opt,arg in opts:
		if opt=="-h":
			print './process_replay.py -r <csv runlist> -c <config>'
			print "config types: 0, 1"
			print "0 - raw + digi + tps"
			print "1 - utca vs vme + reco"
			print "2 - utca vs vme only"
			print "3 - raw + digi + tps + qie10"
			sys.exit()
		elif opt=="-r":
			runlist = arg.split(",")
		elif opt=="-c":
			config = arg
	
	#	validate input
	if not validateInput(runlist, config):
		print "Input is not correct..."
		sys.exit(2)
	config = int(config)
	print "runlist: %s" % str(runlist)
	print "config: %d" % config

	#	get the locks set up
	locks = [Lock() for i in range(len(runlist))]

	# launch cmssw processing
	states = Array('i', len(runlist) )
	for id in range(len(runlist)):
		Process(target=process, args=(id, runlist[id], locks[id], states,
			config)).start()

	#	sleep for 5 secs
	time.sleep(5)

	#	launch uploading
	uploaded = [False for i in range(len(runlist))]
	nups = 0
	while True:
		if nups==len(uploaded):break
		time.sleep(10)
		for i in range(len(runlist)):
			if states[i]==1 and  not uploaded[i]:
				upload(runlist[i], config)
				uploaded[i] = True
				nups+=1

if __name__=="__main__":
	main(sys.argv[1:])
