#!/bin/bash

#
#	Installation script
#

SRC=$1
DEST=$2

cp -r $SRC/Utilities $DEST
export HCALDQMUTILITIES=$DEST/Utilities

echo "Installed HCALDQM Utilities package in $HCALDQMUTILITIES"

