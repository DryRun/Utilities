"""
run Analysis of a local run + Trend plot generation
"""

import sys, os
pathToUtilities = os.environ["HCALDQMUTILITIES"]
sys.path.append(pathToUtilities)

import WBM.Wrapper as dbwrap
import Settings.Settings_Wrapper as settingswrap
import Utils.Shell as Shell

def run(*argv):
	cmssw_config_pathfile = argv[0]
	runFile = argv[1]
	runType = argv[2]
	cmssw_harvesterconfig_pathfile = argv[3]
	listToHarvest = argv[4]
	listRunNumbers = argv[5]
	logfile = argv[6]

#	wbmdir = pathToUtilities+"/"+"WBM/sql_templates"
#	template = "query.sql"
#	dbw = dbwrap.Wrapper(settingswrap.runinfo_db_name,
#		Shell.join(wbmdir, template), logfile)
#	#	check if the old config works - then go ahead
#	o,e,rt = dbw.query(int(runNumber), "CONFIG_NEW")
#	if o=="":
#		o,e,rt = dbw.query(int(runNumber), "CONFIG_OLD")
#	if rt>0 or e!="" or o=="":
#		logfile.write("Problem with Query Run Info DB Step %d %s %s" % (
#			rt, e, o))
#		return 100
#	runType = dbwrap.runinfo_config2runtype(o)
	
	cmd = "cmsRun %s inputFiles=file:%s runType=%s" % (
		cmssw_config_pathfile, runFile, runType 
	)
	print cmd
#	o,e,r = Shell.execute(cmd.split(" "))

	#	don't do any trends for RADDAM
	if "RADDAM" in runType.upper():
		return 0 
	cmd = "cmsRun %s runType=%s runFiles=%s runNumbers=%s" % (
		cmssw_harvesterconfig_pathfile, runType, listToHarvest, listRunNumbers
	)
	print cmd
#	o,e,r = Shell.execute(cmd.split(" "))
	
	#	0 is good - not 0 not good
	return 0

if __name__=="__main__":
	cmssw_config_pathfile = "config"
	runFile = "file.root"
	runNumber = "264825"
	cmssw_harvesterconfig_pathfile = "configharvesting"
	listToHarvest = "listToHarvest"
	listRunNumbers = "listRunNumbers"
	logfile = open("test", "w")
	x = run(cmssw_config_pathfile, runFile, runNumber, cmssw_harvesterconfig_pathfile, listToHarvest, listRunNumbers, logfile)
	print x
