#!/bin/bash

# any future command that fails will exit the script
set -e
# Lets write the public key of our aws instance
eval $(ssh-agent -s)

# touch ~/.ssh/id_rsa
# echo $PRIVATE_KEY > ~/.ssh/id_rsa
# chmod 600 ~/.ssh/id_rsa

# disable the host key checking.
chmod +x ./deploy/disableHostKeyChecking.sh
./deploy/disableHostKeyChecking.sh

# we have already setup the DEPLOYER_SERVER in our gitlab settings which is a
# comma seperated values of ip addresses.
echo "print secrets:$1:end"
DEPLOY_SERVERS=$secrets.DEPLOY_SERVERS
echo "SECRETS-START:${secrets}:END"
# lets split this string and convert this into array
# In UNIX, we can use this commond to do this
# ${string//substring/replacement}
# our substring is "," and we replace it with nothing.
ALL_SERVERS=(${DEPLOY_SERVERS//,/ })
echo "ALL_SERVERS START:${ALL_SERVERS}:END"
exit
# Lets iterate over this array and ssh into each EC2 instance
# Once inside.
# 1. Stop the server
# 2. Take a pull
# 3. Start the server
for server in "${ALL_SERVERS[@]}"
do
  echo "deploying to ${server}"
  ssh ubuntu@${server} 'bash -s' < ./deploy/updateAndRestart.sh
done
