Transition Shell
=====

Description
-----

This project is used to provide a user-friendly interface for bouncing into ATILLA network infrastructure. The repository can be cloned on a user-level account on a server facing the internet. 

If they have the correct access rights (public key or password), external users can connect to the server with `ssh installed-user@server-name`.

Once the user is connected, he can bounce into ATILLA network by entering a specific server address.

Requirements
-----

* `OpenSSH Server`
* `Python3`
* `Python-pip`
* `Python-dialog`

Install
-----

* `git clone git@gitlab.atilla.org:adminsys/transition-shell.git`
* `cd <path-to-repo>`
* `virtualenv -p $(which python3) venv`
* `source venv/bin/activate`
* `pip install -r requirements.txt`
* `adduser --shell <path-to-repo>/init.sh`
