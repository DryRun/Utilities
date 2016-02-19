#!/bin/sh

CMSSWVERSION=$1
LOG=$2
CMSSW=$HCALDQM/CMSSW/$CMSSWVERSION
echo $CMSSW > $LOG

#	setup CMSSW
cd $CMSSW/src
echo $CMSSW/src > $LOG
source /opt/offline/cmsset_default.sh
export SCRAM_ACRCH=slc6_amd64_gcc491
echo $SCRAM_ARCH > $LOG
cmsenv
scram b -j 8 > $LOG

#	setup HCALDQM Utilities
source $HCALDQM/HCALDQM-INSTALLATION/Utilities/env.sh
python $HCALDQMUTILITIES/Processing/scripts/process.py Settings.Settings_process > $LOG
