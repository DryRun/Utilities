#!/bin/sh

LOG=$1
source ~/.bashrc

#	setup CMSSW
source /opt/offline/cmsset_default.sh
export SCRAM_ACRCH=slc6_amd64_gcc491

#	setup HCALDQM Utilities
source $HCALDQM/GUI/current/apps/dqmgui/128/etc/profile.d/env.sh
source $HCALDQM/HCALDQM-INSTALLATION/Utilities/env.sh
python $HCALDQMUTILITIES/Processing/scripts/upload.py Settings.Settings_upload > $LOG
