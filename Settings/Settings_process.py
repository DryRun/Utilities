"""
Settings for the process.py script
"""

from SettingsRunDB_OLD import *
from Logging_Local import *
import Utils.Shell as Shell
from Environment import *
import CMSSW.Harvester_Local as harvester
import CMSSW.Environment_Local as environment
import CMSSW.Analyzer_Local as analyzer

runinfo_db_name = "cms_hcl_runinfo/run2009info"
runinfo_db_querytemplate = pathToUtilities+"/"+"WBM/sql_templates/query.sql"
lockpath = "/tmp/hcaldqm/LOCAL/lock"
poolsource = "/hcaldepot1/data"
filesizelimit = 1500000000
tmptmp = Shell.join(environment.cmsswbase, 
	environment.cmsswversion)
tmptmp = Shell.join(tmptmp, 
	"src/"+environment.cmsswdqmintegration)
cmssw_analyzer_config = Shell.join(tmptmp, analyzer.cmssw_config)
cmssw_harvester_config = Shell.join(tmptmp, harvester.cmssw_config)
firstRunToProcess = 260000
