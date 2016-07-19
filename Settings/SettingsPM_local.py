"""
module to be imported to grab settings
"""

#	for lid=0
lid0["PROCESSINGTYPE"] = "LOCAL"
lid0["DATASOURCEPOOL"]  = "/hcaldepot1/data"
lid0["HOSTNAME"] = "localhost"
lid0["RUNDBSERVERHOSTNAME"] = "localhost"
lid0["RUNDBSERVERPORT"] = 10000 
lid0["LAUNCHMASTERHOSTNAME"] = 'localhost'
lid0["LAUNCHMASTERPORT"] = 30000

#	for lid=1
lid1["PROCESSINGTYPE"] = "LOCAL"
lid1["HOSTNAME"] = "localhost"
lid1["PORT"] = 20001
lid1["RUNDBSERVERHOSTNAME"] = "localhost"
lid1["RUNDBSERVERPORT"] = 10000 

settings = [lid0, lid1]
