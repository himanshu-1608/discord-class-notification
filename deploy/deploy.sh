#!/bin/bash
set -e
# disable the host key checking.
chmod +x ./deploy/disableHostKeyChecking.sh
./deploy/disableHostKeyChecking.sh
DEPLOY_SERVERS=$DEPLOY_SERVERS
# lets split this string and convert this into array
# In UNIX, we can use this commond to do this
# ${string//substring/replacement}
# our substring is "," and we replace it with nothing.
ALL_SERVERS=(${DEPLOY_SERVERS//,/ })

chmod 400 $PEM_FILE_PATH

for server in "${ALL_SERVERS[@]}"
do
  echo "deploying to ${server}"
  ssh -i $PEM_FILE_PATH ubuntu@${server} 'bash -s' < ./deploy/updateAndRestart.sh
done
