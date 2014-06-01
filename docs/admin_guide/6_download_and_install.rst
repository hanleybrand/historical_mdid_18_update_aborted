Download and Install
====================

Create the directory where MDID3 will be installed as root, and then
chown it to the account that will run the web app processes

::

    cd /var/local
    sudo mkdir /var/local/mdid
    sudo chown mdid:mdid /var/local/mdid
    sudo chmod 775 /var/local/mdid
    sudo su mdid

Git MDID3!
~~~~~~~~~~

The next command clones the mdid repo into the mdid directory you just
made

::

    git clone git://github.com/cit-jmu/rooibos.git /var/local/mdid 

And if you are going to make any changes, do yourself a favor and make
your own branch right away (this will save you hassle when updating in
the future).

::

    git checkout -b localSite upstream/master

Just in case
^^^^^^^^^^^^

This step may be necessary if you execute git via root in your mdid3
directories, or if for any other reason the mdid user isn't the owner of
var/local/mdid

::

    sudo chown -R mdid:staff /var/local/mdid/*
