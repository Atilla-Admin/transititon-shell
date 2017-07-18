#!/bin/sh

USER_NAME="transition"
HOME_DIR="/home/$USER_NAME"

REPO_URL="https://gitlab.atilla.org/adminsys/transition-shell.git"

# By default, the transition shell will be installed in /home/<user>/transition-shell
BASE_DIR=$HOME_DIR
SHELL_DIR="transition-shell"

echo Installing requirements ...
apt install -y git python3 python3-pip python3-virtualenv

echo Creating new user $USER_NAME ...
adduser --shell $BASE_DIR/$SHELL_DIR/init.sh --disabled-password --system $USER_NAME

# We create the ~/.ssh/authorized_keys file as root in order to avoid unattended edits
echo Creating authorized_keys file ...
mkdir -p $HOME_DIR/.ssh
touch $HOME_DIR/.ssh/authorized_keys

# Setup the project
echo Installing project files ...
cd $BASE_DIR
su -s /bin/sh -c "git clone $REPO_URL $SHELL_DIR" $USER_NAME
cd $SHELL_DIR
su -s /bin/sh -c "virtualenv -p \$(which python3) venv" $USER_NAME
su -s /bin/sh -c ". venv/bin/activate && pip3 install -r requirements.txt" $USER_NAME

echo "
====================
Setup complete !
====================
You can now add authorized keys in $HOME_DIR/.ssh/authorized_keys
and then login with :

ssh $USER_NAME@$(hostname -f)

Note that the files of transition-shell are available in $BASE_DIR/$SHELL_DIR"
