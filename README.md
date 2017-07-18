Transition Shell
=====

Description
-----

This project is used to provide a user-friendly interface for bouncing into ATILLA network infrastructure. The repository can be cloned on a user-level account on a server facing the internet. 

If they have the correct access rights (public key or password), external users can connect to the server with `ssh installed-user@server-name`.

Once the user is connected, he can bounce into ATILLA network by entering a specific server address.

Requirements
-----

* `openssh-server`
* `git`
* `python3`
* `python3-virtualenv`
* `python3-pip`

Automated installation
-----

If you are lazy, you get a quick setup of the project by running as `root`:

```
curl -o- -L https://gitlab.atilla.org/adminsys/transition-shell/raw/master/install.sh | bash
```

... or, if you don’t have `curl` installed on your machine, try:

```
wget -qO- https://gitlab.atilla.org/adminsys/transition-shell/raw/master/install.sh | bash
```

Manual installation
-----

* `git clone git@gitlab.atilla.org:adminsys/transition-shell.git`
* `cd <path-to-repo>`
* `virtualenv -p $(which python3) venv`
* `source venv/bin/activate`
* `pip3 install -r requirements.txt`
* `adduser --shell <path-to-repo>/init.sh --disable-password --system`
