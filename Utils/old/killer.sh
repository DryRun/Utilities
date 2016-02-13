

#
#	Killer script
#	Runs to kill stucked cmsRun jobs
#	Intend to run every 10mins to check if there are running cmsRun processses 
#	that have been running for at least 10mins and kill then
#

#	constants
MAXRUNTIME=600
LOGFILE=/tmp/killer.log

date > $LOGFILE

#	get the id and run time
PROCESSID=`ps aux | grep "[c]msRun " | awk '{print$2}'`
NUMSECONDS=`ps aux | grep "[c]msRun " | awk  '{print $10}' | awk -F: '{print ($1*60) + ($2) }'`

if [[ $NUMSECONDS -gt $MAXRUNTIME ]]; then
	echo "Killing ProcessId: $PROCESSID" > $LOGFILE
	echo "Which already Runs For $NUMSECONDS seconds" > $LOGFILE
	kill -9 $PROCESSID
fi





