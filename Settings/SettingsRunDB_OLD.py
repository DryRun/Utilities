"""
Settings for the OLD-style Run DB
"""

from SettingsRunDB import configurations

dbpool = "/data/hcaldqm/DBLIKE"
dqmiopool = "/data/hcaldqm/DQMIO"
localrunlabel = "COMMISSIONING"
processingtype = "LOCAL"
numrunsForTrend = 30
runtypes = []
for c in configurations:
	runtypes[len(runtypes):] = [c.upper()]

