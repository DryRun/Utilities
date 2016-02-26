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
useMap = True
dbMap = False
globaltag = "run2_hlt"
emaptag = "HcalElectronicsMap_v7.00_offline"
emapfileInPath = "version_G_emap_all_ngHF2016_feb24.txt" #should sit in $CMSSW/src
nameToImport = "CMSSW.Analyzer_Local"
