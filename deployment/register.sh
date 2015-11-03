#!/bin/sh

#
#	Registration Script
#

date

#	predefine paths
DATAPOOL=/nfshome0/hcaldqm/HCALDQM/scripts/output
WORKDIR=/nfshome0/hcaldqm/HCALDQM/scripts
DQMGUI=/nfshome0/hcaldqm/HCALDQM/GUI
TMPSTORAGE=/nfshome0/hcaldqm/HCALDQM/scripts/temporary
FILENAMEBASE=DQM_V0001_Hcal_R000
LENGTHFILENAMEBASE=${#FILENAMEBASE}
DEBUG=$1
HTTPADDRESS="http://hcaldqm01.cms:8060/dqm/dev"
STATUSDIR=/nfshome0/hcaldqm/HCALDQM/scripts/status


if [[ $DEBUG == 1 ]]; then
	echo "DataPool: $DATAPOOL"
fi


if [[ -e $WORKDIR/register.lock ]]; then
	exit
fi


touch $WORKDIR/register.lock

#	Initialize env vars
source $DQMGUI/current/apps/dqmgui/128/etc/profile.d/env.sh


getRunType(){
	#	$1 - Run Number
	#	$2 - Directory for that Run
	str=`cat $2/$1.txt | awk '{print $3}'`
	str=${str^^}
	if [[ $str == *"PEDESTAL"* ]]; then
		echo "Pedestal"
	elif [[ $str == *"LED"* ]]; then
		echo "Led"
	elif [[ $str == *"RADDAM"* ]]; then
		echo "Raddam"
	elif [[ $str == *"LASER"* ]]; then
		echo "Laser"
	else
		echo "Unknown"
	fi
}


getYear(){
	#	$1 - Run Number
	#	$2 - Directory
	str=20`cat $2/$1.txt | awk '{print $4}' | awk -F- '{print $3}'`
	echo $str
}


genFileToUpload(){
	#	$1 FILENAME as input	
	#	#2 RUNTYPE
	#	#3 Year
	#	#4 RUNNUMBER
	GENNAME=$TMPSTORAGE/DQM_V0001_R000$4__$2__Commissioning$3__DQMIO.root
	cp $1 $GENNAME
	echo $GENNAME
}


#	list all the directories containing root files
#	and index them if they haven't been yet
if [[ $DEBUG == 1 ]]; then
	echo "Starting the Loop"
else
	echo "Starting the Loop"
fi
for DIR in $DATAPOOL/DQM_V0001_Hcal_*; do
	#	Some RUNNUMBER extraction
	LENGTHBASE=${#DIR}
	POS=`expr $LENGTHBASE + 1 + $LENGTHFILENAMEBASE`
	LENGTH=6
	FILENAME=`ls $DIR/*.root`
	RUNNUMBER="${FILENAME:$POS:$LENGTH}"
	if [[ -e $STATUSDIR/failed/$RUNNUMBER ]]; then
		continue
	fi
	if [[ ! -e $STATUSDIR/processed/$RUNNUMBER ]]; then
		continue
	fi
	RUNTYPE=`getRunType $RUNNUMBER $DIR`
	YEAR=`getYear $RUNNUMBER $DIR`

	if [[ $DEBUG == 1 ]]; then
		echo "LengthBase: $LENGTHBASE"
		echo "POS: $POS"
		echo "FileName: $FILENAME"
		echo "RunNumber: $RUNNUMBER"
		echo "RunType: $RUNTYPE"
		echo "Year: $YEAR"
	fi

	#	If it's been registered, skip
	if [[ ! -e $DQMGUI/indexed/$RUNNUMBER ]]; then
		FILENAMETOUPLOAD=`genFileToUpload $FILENAME $RUNTYPE $YEAR $RUNNUMBER`
		if [[ $DEBUG == 1 ]]; then
			echo "Uploading FileName: $FILENAMETOUPLOAD"
		else
			echo "Uploadin FileName: $FILENAMETOUPLOAD"
			if visDQMUpload $HTTPADDRESS $FILENAMETOUPLOAD; then
				touch $DQMGUI/indexed/$RUNNUMBER
			else
				touch $DQMGUI/failed/$RUNNUMBER
			fi
		fi
		rm $FILENAMETOUPLOAD
	fi
done

trap "rm $WORKDIR/register.lock; exit " SIGINT INT TERM EXIT






