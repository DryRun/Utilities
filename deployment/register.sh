#!/bin/sh

#
#	Registration Script
#

#	predefine paths
DATAPOOL=/nfshome0/hcaldqm/HCALDQM/scripts/output
DQMGUI=/nfshome0/hcaldqm/HCALDQM/GUI
FILENAMEBASE=DQM_V0001_Hcal_R000
LENGTHFILENAMEBASE=${#FILENAMEBASE}
LOGFILE="/tmp/register.log"
DEBUG=$1

if [[ $DEBUG == 1 ]]; then
	echo "DataPool: $DATAPOOL"
fi

if [[ -e register.lock ]]; then
	exit
fi

touch register.lock

#	Initialize env vars
source $DQMGUI/current/apps/dqmgui/128/etc/profile.d/env.sh

#	list all the directories containing root files
#	and index them if they haven't been yet
for DIR in $DATAPOOL/DQM_V0001_Hcal_*; do

	#	Some RUNNUMBER extraction
	LENGTHBASE=${#DIR}
	POS=`expr $LENGTHBASE + 1 + $LENGTHFILENAMEBASE`
	LENGTH=6
	FILENAME=`ls $DIR/*`
	RUNNUMBER="${FILENAME:$POS:$LENGTH}"

	if [[ $DEBUG == 1 ]]; then
		echo "LengthBase: $LENGTHBASE"
		echo "POS: $POS"
		echo "FileName: $FILENAME"
		echo "RunNumber: $RUNNUMBER"
	fi

	#	If it's been registered, skip
	if [[ ! -e $DQMGUI/indexed/$RUNNUMBER ]]; then
		if [[ $DEBUG == 1 ]]; then
			echo "Indexing FileName: $FILENAME"
		else
			echo "Indexing FileName: $FILENAME" > $LOGFILE
			if visDQMIndex add --dataset /Global/Online/ALL $DQMGUI/state/dqmgui/dev/ix128 $FILENAME > $LOGFILE; then
				touch $DQMGUI/indexed/$RUNNUMBER
			else
				touch $DQMGUI/failed/$RUNNUMBER
			fi
		fi
	fi
done

trap "rm register.lock; exit " SIGINT INT TERM EXIT






