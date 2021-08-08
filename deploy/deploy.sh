#!/bin/bash

# any future command that fails will exit the script
set -e
# Lets write the public key of our aws instance
eval $(ssh-agent -s)
# echo "$2" | ssh-add - > /dev/null
# touch ~/.ssh/id_rsa
# echo $PRIVATE_KEY > ~/.ssh/id_rsa
# chmod 600 ~/.ssh/id_rsa

# disable the host key checking.
chmod +x ./deploy/disableHostKeyChecking.sh
./deploy/disableHostKeyChecking.sh

# we have already setup the DEPLOYER_SERVER in our gitlab settings which is a
# comma seperated values of ip addresses.
DEPLOY_SERVERS=$1
# lets split this string and convert this into array
# In UNIX, we can use this commond to do this
# ${string//substring/replacement}
# our substring is "," and we replace it with nothing.
ALL_SERVERS=(${DEPLOY_SERVERS//,/ })

echo $2 > himanshu-ssh-keypair.pem

chmod 400 himanshu-ssh-keypair.pem

# echo $(<himanshu-ssh-keypair.pem)
ls

for server in "${ALL_SERVERS[@]}"
do
  echo "deploying to ${server}" # | sed 's/./& /g'
  # ssh -i ./ssh_key.pem ubuntu@${server} 'bash -s' < ./deploy/updateAndRestart.sh
  ssh -i "himanshu-ssh-keypair.pem" ubuntu@${server} 'bash -s' < ./deploy/updateAndRestart.sh
done
