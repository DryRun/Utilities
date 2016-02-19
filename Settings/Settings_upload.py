"""
Settings for the process.py script
"""

from SettingsRunDB_OLD import *
from Logging_Local import *
import Utils.Shell as Shell
from Environment import *

runinfo_db_name = "cms_hcl_runinfo/run2009info"
runinfo_db_querytemplate = pathToUtilities+"/"+"WBM/sql_templates/query.sql"
lockpath = "/tmp/hcaldqm/LOCAL/lock.upload"
hostname = "http://fu-c2f11-21-03.cms:8070/dqm/online-dev"
logfilename = "/tmp/hcaldqm/LOCAL/log.upload"
regexppattern = "^DQM_V(\d+)_R(\d+)((__[-A-Za-z0-9_]+){3})\.root$"
