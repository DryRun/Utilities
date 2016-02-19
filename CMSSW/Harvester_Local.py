"""
setting CMSSW Local EDAnalyzer paramters
"""

#	general
cmssw_config = "hcal_harvester_test_cfg.py"

#	dqmgui
dqmguiconvention = "Offline"
dqmiopool = '/data/hcaldqm/DQMIO/LOCAL'

#	cmssw
useMap = True
dbMap = False
globaltag = "74X_dataRun2_Express_v2"
emaptag = "HcalElectronicsMap_v7.00_offline"
emapfileInPath = "version_G_emap_2015_may_20"
nameToImport = "CMSSW.Harvester_Local"
