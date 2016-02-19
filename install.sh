#!/bin/bash

#
#	Installation script
#

DEST=$1
SRC=`dirname ${BASH_SOURCE[0]}`

cp -r $SRC $DEST
mkdir $DEST/LOGS
source $DEST/Utilities/env.sh

echo "Installed HCALDQM Utilities package in $DEST/Utilities"
echo "HCALDQM LOGs are in $DEST/LOGS"

