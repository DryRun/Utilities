"""
run Analysis of a local run + Trend plot generation
"""

import sys, os
pathToUtilities = os.environ["HCALDQMUTILITIES"]
sys.path.append(pathToUtilities)

import WBM.Wrapper as dbwrap
import Settings.Settings_Wrapper as settingswrap
import Utils.Shell as Shell

def process(*argv):
	runFile = argv[0]
	runType = argv[1]
	settings = argv[2]
	logfile = argv[3]

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
	
	cmd = "cmsRun %s inputFiles=file:%s runType=%s settingsModuleName=%s" % (
		settings.cmssw_analyzer_config, runFile, runType, 
		settings.analyzer.nameToImport
	)
	logfile.write(cmd+"\n")
	o,e,r = Shell.execute(cmd.split(" "))
	print "OUTPUT Stream:\n"+o+"\n"+("-"*50)+"\n"
	print "ERROR Stream:\n"+e+"\n"+("-"*50)+'\n'
	return 0

	#	don't do any trends for RADDAM
#	if "RADDAM" in runType.upper():
#		return 0 
#	cmd = "cmsRun %s runType=%s runFiles=%s runNumbers=%s settingsModuleName=%s" % (
#		settings.cmssw_harvester_config, runType, listToHarvest, listRunNumbers,
#		settings.harvester.nameToImport
#	)
#	logfile.write(cmd)
#	o,e,r = Shell.execute(cmd.split(" "))
	
	#	0 is good - not 0 not good
#	return 0

if __name__=="__main__":
	pass
