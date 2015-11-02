#!/bin/sh

#
#	Processing Script
#	Processes Local HCALDQM Runs
#

#	predefine paths/variables
DATAPOOL=/hcaldepot1/data
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
DESTPOOL=/hcaldepot1/DetDiag/LOCAL_HTML/

#
#	Input Options
#	3 - Processing Options
#		0 - Regular processing
#		1 Reprocess 1 run with $4 as runNumber
#		2 Reprocess all with $4 as minRunNumber
#
LONGSHORT=$1
DEBUG=$2
OPTION=$3

if [[ $DEBUG == 1 ]]; then
	echo "Pool: $DATAPOOL"
	echo "LongShort: $LONGSHORT"
fi

#
#	Determine if there is a lock set.
#	2 lock types for 2 processing types short/long
#	if there is a lock of your type - exit
#
LOCKFILE="$WORKDIR/process.lockshort"
if [[ $LONGSHORT == "LONG" ]]; then
	LOCKFILE="$WORKDIR/process.locklong"
fi
if [[ -e $LOCKFILE ]]; then
	exit 0
else
	touch $LOCKFILE
fi

if [[ $DEBUG == 1 ]]; then
	echo $LOCKFILE
fi

#	Initialize env vars
cd $CMSSWSRC
source /opt/offline/cmsset_default.sh
export SCRAM_ACRCH=slc6_amd64_gcc491
cmsenv
scram b -j 8
cd $WORKDIR

cleanAll() {
	rm $STATUSDIR/failed/*
	rm $STATUSDIR/processing/*
	rm $STATUSDIR/processed/*
}

clean1() {
	rm $STATUSDIR/failed/$1
	rm $STATUSDIR/processing/$1
	rm $STATUSDIR/processed/$1
}

copy1() {
	mkdir $DQMOUTPUT/DQM_V0001_Hcal_R000$1_0
	mv $WORKDIR/DQM_V0001_Hcal_R000$1.root $DQMOUTPUT/DQM_V0001_Hcal_R000$1_0
	cp -r $DQMOUTPUT/DQM_V0001_Hcal_R000$1_0 $DESTPOOL 

}

process() {
	#	List all files that are available in the pool
	echo "Startign the Loop"
	for FILE in $DATAPOOL/USC_*.root; do
	
		#	get the run number
		LENGTHBASE=${#DATAPOOL}
		LENGTHFILENAMEBASE=${#FILENAMEBASE}
		POS=`expr $LENGTHBASE + 1 + $LENGTHFILENAMEBASE`
		LENGTH=6
		RUNNUMBER="${FILE:$POS:$LENGTH}"
		LOGFILE="$LOGFILEBASE.$RUNNUMBER"
		FILESIZE=`ls -l $FILE | awk '{print $5}'`
	
		if [[ $DEBUG == 1 ]]; then
			echo "Filename: $FILE"
			echo "LengthBase:  $LENGTHBASE"
			echo "LengthFilenameBase: $LENGTHFILENAMEBASE"
			echo $POS
			echo "Length: $LENGTH"
			echo "RunNumber: $RUNNUMBER"
			echo "LogFile: $LOGFILE"
			echo "FileSize: $FILESIZE"
		fi
	
		#	Decide if we want to process this run or not, based on
		#	1. FILESIZE
		#	2. MINRUNNUMBER - either $MINRUNNUMBER or what is provided to the func
		if [[ $RUNNUMBER -lt $1 ]]; then
			continue
		fi
		if [[ $LONGSHORT == "LONG" && $FILESIZE -lt $SIZETHRESHOLD ]]; then
			continue
		fi
		if [[ $LONGSHORT == "SHORT" && $FILESIZE -gt $SIZETHRESHOLD ]]; then
			continue
		fi
		
		#	do the cmsRun if this file isn't present
		if [[ -e $STATUSDIR/processing/$RUNNUMBER ]]; then
			continue
		fi
		if [[ ! -e $STATUSDIR/processed/$RUNNUMBER ]]; then
			echo "Processing FileName: $FILE" > $LOGFILE
			if [[ $DEBUG == 1 ]]; then
				echo "DEBUG: cmsRun $WORKDIR/hcal_dqm_local_cfg.py inputFiles=file:$FILE"
			else
				touch $STATUSDIR/processing/$RUNNUMBER
				if cmsRun $WORKDIR/hcal_dqm_local_cfg.py inputFiles=file:$FILE	\
					> $LOGFILE 2>&1; then
					touch $STATUSDIR/processed/$RUNNUMBER
					copy1($RUNNUMBER)
				else
					touch $STATUSDIR/failed/$RUNNUMBER
					rm $STATUSDIR/processing/$RUNNUMBER
				fi
			fi
		fi
	done
}

process1() {
	if [[ $DEBUG == 1 ]]; then
		echo "DEBUG: cmsRun $WORKDIR/hcal_dqm_local_cfg.py inputFiles=file:$DATAPOOL/USC_$1.root"
	else
		touch $STATUSDIR/processing/$1
		if cmsRun $WORKDIR/hcal_dqm_local_cfg.py inputFiles=file:$DATAPOOL/USC_$1.root; then
			touch $STATUSDIR/processed/$1
			copy1($1)
		else
			touch $STATUSDIR/failed/$1
			rm $STATUSDIR/processing/$1
		fi
	fi
}

if [[ $OPTION == 0 ]]; then
	process($MINRUNNUMBER)
elif [[ $OPTION == 1 ]]; then
	cleanAll()
	process($4)
elif [[ $OPTION == 2 ]]; then
	clean1($4)
	process1($4)	
fi

#	set up the trap
trap "rm $LOCKFILE; exit" SIGINT INT TERM EXIT










