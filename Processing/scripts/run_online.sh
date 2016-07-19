#!/bin/sh

CMSSWVERSION=CMSSW_8_0_9
CMSSWCONFIG=$2

source ~/.bashrc
CMSSW=$HCALDQM/CMSSW_PLAYBACK/$CMSSWVERSION

cd $CMSSW/src
source /opt/offline/cmsset_default.sh
export SCRAM_ACRCH=slc6_amd64_gcc493
cmsenv


CMSSWCONFIGPATH=$CMSSW/src/DQM/Integration/python/clients
echo $CMSSWCONFIGPATH
cmsRun $CMSSWCONFIGPATH/$CMSSWCONFIG runNumber=$1 skipFirstLumis=False scanOnce=True runInputDir=/fff/BU0/output/lookarea
