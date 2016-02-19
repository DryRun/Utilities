"""
Setting CMSSW Local EDAnalyzer paramters
to be imported into the actual cmsRun config
"""

#	general
cmssw_config = "hcal_dqm_local_test_cfg.py"

#	dqm gui
dqmguiconvention = 'Offline'
dqmiopool = '/data/hcaldqm/DQMIO/LOCAL'

#	cmssw
useMap = False
dbMap = False
globaltag = "74X_dataRun2_Express_v2"
emaptag = "HcalElectronicsMap_v7.00_offline"
emapfileInPath = "version_G_emap_2015_may_20" #should sit in $CMSSW/src
nameToImport = "CMSSW.Analyzer_Local"
