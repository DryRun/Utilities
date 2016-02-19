#!/bin/bash

DIR=$1

source current/apps/dqmgui/128/etc/profile.d/env.sh

# should be given $2=8070
# should be given $3=online-dev 
for FILE in $DIR/DQM_*.root;do
	visDQMUpload http://fu-c2f11-21-03.cms:$2/dqm/$3 $FILE
done



