#!/bin/sh

#
#	Processing Script
#	Processes Local HCALDQM Runs
#

#	predefine paths/variables
DATAPOOL=/hcaldepot1/data
FILENAMEBASE=USC_
SERVERLOG=/tmp/process.log.server
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
#		PROCESSALL - Process all starting with $MINRUNNUMBER
#		REPROCESSALL - reprocess all with $4 as minRunNumber
#		REPROCESS1 - Reprocess 1 run with $4 as runNumber
#		PROCESS1 - Process 1 new run with $4 as Run Number
#
LONGSHORT=$1
DEBUG=$2
OPTION=$3

if [[ $DEBUG == 1 ]]; then
	echo "Pool: $DATAPOOL"
	echo "LongShort: $LONGSHORT"
	echo "Option: $OPTION"
	if [[ $OPTION != "PROCESSALL" ]]; then
		echo "Additional Argument: $4"
	fi
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

#	Debugging
echo "Starting..." > $SERVERLOG
date > $SERVERLOG

#	Initialize env vars
cd $CMSSWSRC
source /opt/offline/cmsset_default.sh
export SCRAM_ACRCH=slc6_amd64_gcc491 
cmsenv
scram b -j 8 > $SERVERLOG
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
	if [[ ! -e $DQMOUTPUT/DQM_V0001_Hcal_R000$1_0 ]]; then
		mkdir $DQMOUTPUT/DQM_V0001_Hcal_R000$1_0
	fi
	DESTINATION=$DQMOUTPUT/DQM_V0001_Hcal_R000$1_0
	mv $WORKDIR/DQM_V0001_Hcal_R000$1.root $DESTINATION
	mv $1.xml $1.txt $DESTINATION
	cp -r $DESTINATION $DESTPOOL 
}

process() {
	#	List all files that are available in the pool
	echo "Starting the Loop"
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
			if [[ -e $STATUSDIR/failed/$RUNNUMBER ]]; then
				rm $STATUSDIR/failed/$RUNNUMBER
			fi
			echo "START Processing FileName: $FILE" > $SERVERLOG
			date > $SERVERLOG
			if [[ $DEBUG == 1 ]]; then
				echo "DEBUG: ./cmsRun_local.py $FILE $RUNNUMBER $WORKDIR $LOGFILE"
			else
				echo "Start Processing $FILE" >> $LOGFILE
				touch $STATUSDIR/processing/$RUNNUMBER
				if ./cmsRun_local.py $FILE $RUNNUMBER $WORKDIR $LOGFILE >> $LOGFILE; then
					touch $STATUSDIR/processed/$RUNNUMBER
					copy1 $RUNNUMBER
				else
					touch $STATUSDIR/failed/$RUNNUMBER
					rm $STATUSDIR/processing/$RUNNUMBER
					echo "FAILED" > $SERVERLOG
				fi
				echo "End Processing $FILE" >> $LOGFILE
			fi
			date > $SERVERLOG
			echo "END Processing FileName: $FILE" > $SERVERLOG
		fi
	done
}

process1() {
	if [[ -e $STATUSDIR/failed/$1 ]]; then
		rm $STATUSDIR/failed/$1
	fi
	if [[ $DEBUG == 1 ]]; then
		echo "DEBUG: ./cmsRun_local.py $DATAPOOL/USC_$1.root $1 $WORKDIR tmp.log"
	else
		echo "Start Processing Run: $1"
		date
		touch $STATUSDIR/processing/$1
		if ./cmsRun_local.py $DATAPOOL/USC_$1.root $1 $WORKDIR tmp.log; then
			touch $STATUSDIR/processed/$1
			copy1 $1
		else 
			touch $STATUSDIR/failed/$1
			rm $STATUSDIR/processing/$1
			echo "FAILED"
		fi
		date 
		echo "End Processing Run: $1"
	fi
}

if [[ $OPTION == "PROCESSALL" ]]; then
	if [[ $DEBUG == 1 ]]; then
		echo "Regular Processing of all starting with $MINRUNNUMBER"
	fi
	process $MINRUNNUMBER
elif [[ $OPTION == "REPROCESSALL" ]]; then
	if [[ $DEBUG == 1 ]]; then
		echo "Reprocessing of starting with $4"
	fi
	cleanAll 
	process $4
elif [[ $OPTION == "REPROCESS1" ]]; then
	if [[ $DEBUG == 1 ]]; then
		echo "Reprocessing a single RunNumber $4"
	fi
	clean1 $4
	process1 $4
elif [[ $OPTION == "PROCESS1" ]]; then
	if [[ $DEBUG == 1 ]]; then
		echo "Process a single Run $4"
	fi
	process1 $4
fi

#	set up the trap
trap "rm $LOCKFILE; exit" SIGINT INT TERM EXIT










