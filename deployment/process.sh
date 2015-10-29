#!/bin/sh

#
#	Processing Script
#	Processes Local HCALDQM Runs
#

#	predefine paths/variables
DATAPOOL=/hcaldepot1/data/
FILENAMEBASE=USC_
LOGFILEBASE=/tmp/process.log
CMSSWDIR=/nfshome0/hcaldqm/HCALDQM/CMSSW
CMSSWVERSION=CMSSW_7_4_15
CMSSWSRC=$CMSSWDIR/$CMSSWVERSION/src
WORKDIR=/nfshome0/hcaldqm/HCALDQM/scripts
STATUSDIR="$WORKDIR/status"
DQMOUTPUT=$WORKDIR/output
MINRUNNUMBER=250000
SIZETHRESHOLD=600000000
LONGSHORT=$1
DEBUG=$2

#
#	Determine if there is a lock set.
#	2 lock types for 2 processing types short/long
#	if there is a lock of your type - exit
#
$LOCKFILE=$WORKDIR/process.lockshort
if [[ $LONGSHORT=="LONG" ]]; then
	LOCKFILE=$WORKDIR/process.locklong
fi
if [[ -e $LOCKFILE ]]
	exit 0
else
	touch $LOCKFILE
fi

#	Initialize env vars
cd $CMSSWSRC
source /opt/offline/cmsset_default.sh
export SCRAM_ACRCH=slc6_amd64_gcc491
eval `cmsenv`
eval `scram b -j 8`
cd $WORKDIR

#	List all files that are available in the pool
for FILE in $DATAPOOL/USC_*.root; do

	#	get the run number
	LENGTHBASE=${#DATAPOOL}
	LENGTHFILENAMEBASE=${#FILENAMEBASE}
	POS=`expr $LENGTHBASE + 1 + $LENGTHFILENAMEBASE`
	LENGTH=6
	RUNNUMBER="${FILE:$POS:$LENGTH}"
	LOGFILE="$LOGFILEBASE.$RUNNUMBER"
	FILESIZE=`ls -l $FILE | awk '{print $5}'`

	#	Decide if we want to process this run or not, based on
	#	1. FILESIZE
	#	2. MINRUNNUMBER
	if [[ $RUNNUMBER -lt $MINRUNNUMBER ]]; then
		continue
	fi
	if [[ $LONGSHORT == "LONG" && $FILESIZE -lt $SIZETHRESHOLD ]]; then
		continue
	fi
	if [[ $LONGSHORT == "SHORT" && $FILESIZE -gt $SIZETHRESHOLD ]]; then
		continue
	fi
	
	#	do the cmsRun if this file isn't present
	if [[ -e $STATUSDIR/status/processing/$RUNNUMBER ]]; then
		continue
	fi
	if [[ ! -e $STATUSDIR/status/processed/$RUNNUMBER ]]; then
		echo "Processing FileName: $FILE" > $LOGFILE
		touch $STATUSDIR/status/processing/$RUNNUMBER
		if [[ $DEBUG==1 ]]; then
			echo "DEBUG: cmsRun $WORKDIR/hcal_dqm_local_cfg.py inputFiles=$FILE"
		else

			if cmsRun $CMSSWDQM/new_hcal_dqm_Local.py inputFiles=$FILE	\
				> $LOGFILE 2>&1; then
				touch $STATUSDIR/status/processed/$RUNNUMBER
			else
				touch $STATUSDIR/status/failed/$RUNNUMBER
				rm $STATUSDIR/status/processing/$RUNNUMBER
			fi
		fi
	fi
done

#	Release the lock!
rm $LOCKFILE

#	set up the trap
trap "rm $LOCKFILE; exit" INT TERM EXIT










