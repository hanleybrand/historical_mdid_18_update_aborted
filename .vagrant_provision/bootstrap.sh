#!/usr/bin/env bash

echo -e "################# Provisioning vagrant box via ./vagrant_provision/bootstrap.sh #################"

HOME_DIR=`pwd`
VAGRANT_DIR=/vagrant
PROVISION_DIR=$VAGRANT_DIR/.vagrant_provision
MDID_DIR=$HOME_DIR/mdid
MDID_DATA_DIR=$HOME_DIR/mdid-data
CONFIG_DIR=$MDID_DIR/config
ROOIBOS_DIR=$MDID_DIR/rooibos

sudo -u vagrant mkdir -p bootstrap_logs


##############################################################################
# A Vagrant provisioning shell script to setup an MDID Development VM
##############################################################################

echo -e "################# Making sure system & apt-get are up to date #################"

# add ppa for ffmpeg
add-apt-repository ppa:mc3man/trusty-media 1>> bootstrap_logs/install.txt 2>> bootstrap_logs/install_errors.txt

# Update our apt sources
apt-get update 1>> bootstrap_logs/install.txt 2>> bootstrap_logs/install_errors.txt

# Make sure we are starting from an up-to-date system
apt-get upgrade -y 1>> bootstrap_logs/install.txt 2>> bootstrap_logs/install_errors.txt
apt-get dist-upgrade -y 1>> bootstrap_logs/install.txt 2>> bootstrap_logs/install_errors.txt

echo -e "################# Installing MySQL, Solr, RabbitMQ, memcached #################"

# The mysql-server package interactively prompts for the root pasword to the
# MySQL server.  These commands will cache the password settings, and they
# will be used by the mysql-server package on installation.  Since this is
# pretty insecure anyway, no attempt is made at using a secure password :)
#
# Sets the MySQL root password to 'rooibos' to conform to existing docs, etc.

echo -e "\n\n                  PSSST:  the mysql root password is: rooibos\n\n"

echo mysql-server mysql-server/root_password password rooibos | debconf-set-selections
echo mysql-server mysql-server/root_password_again password rooibos | debconf-set-selections

# Now we can install the packages
# mysql-server: The MySQL server
# mysql-client: The MySQL client utilities
# libmysqlclient-dev: MySQL developmental libraries, needed to build the python
#   MySQL module
apt-get install -y mysql-server mysql-client libmysqlclient-dev 1>> bootstrap_logs/install.txt 2>> bootstrap_logs/install_errors.txt

##############################################################################
# Install other dependencies
##############################################################################

# Java is needed to run Solr
apt-get install -y openjdk-7-jre-headless 1>> bootstrap_logs/install.txt 2>> bootstrap_logs/install_errors.txt

# RabbitMQ is needed to manage the worker jobs
apt-get install -y rabbitmq-server 1>> bootstrap_logs/install.txt 2>> bootstrap_logs/install_errors.txt

# Memcached is used for django's memory object cache
apt-get install -y memcached 1>> bootstrap_logs/install.txt 2>> bootstrap_logs/install_errors.txt

##############################################################################
# Python build dependencies
##############################################################################

echo -e "################# Installing python things that require apt-get #################"

apt-get install -y python-dev 1>> bootstrap_logs/install.txt 2>> bootstrap_logs/install_errors.txt

# PyODBC needs the unixodbc libs
apt-get install -y unixodbc unixodbc-dev 1>> bootstrap_logs/install.txt 2>> bootstrap_logs/install_errors.txt

# python-ldap needs ldap and sasl libraries
apt-get install -y libldap2-dev libsasl2-dev 1>> bootstrap_logs/install.txt 2>> bootstrap_logs/install_errors.txt

# Pillow needs image libraries
apt-get install -y libtiff5-dev libjpeg8-dev zlib1g-dev 1>> bootstrap_logs/install.txt 2>> bootstrap_logs/install_errors.txt

# ffmpeg for video funage
apt-get install -y ffmpeg 1>> bootstrap_logs/install.txt 2>> bootstrap_logs/install_errors.txt


##############################################################################
# Setup files and directories
##############################################################################

echo -e "################# Setting up files & directories as vagrant user #################"

# create a symlink from /vagrant to our home dir
sudo -u vagrant ln -s $VAGRANT_DIR $MDID_DIR

# create directories for our mdid data
sudo -u vagrant mkdir -p $MDID_DATA_DIR
# explicitly create the log directory, because when the workers service fires
# up later in the provisioning, if they're not there then they will get
# created by root and permissions will be all jacked up
sudo -u vagrant mkdir -p $MDID_DATA_DIR/scratch/logs

# link in a little helper script for running the django dev server
sudo -u vagrant ln -s $PROVISION_DIR/runserver $HOME_DIR/

##############################################################################
# Configure Python and setup a Virtual Environment
##############################################################################
# Use PIP for python package management

echo -e "################# Configuring Python and setting up Virtual Environment #################"


apt-get install -y python-pip 1>> bootstrap_logs/install.txt 2>> bootstrap_logs/install_errors.txt

echo -e "################# Installing virtualenv software #################"

# install virtualenv
# as per docs, virtualenv & vewrapper should only be installed in a system install of python
# http://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation

WORKON_HOME=$HOME/.virtualenvs

pip install --upgrade virtualenv 1>> bootstrap_logs/install.txt 2>> bootstrap_logs/install_errors.txt
pip install --upgrade virtualenvwrapper 1>> bootstrap_logs/install.txt 2>> bootstrap_logs/install_errors.txt

sudo -u vagrant mkvirtualenv -a $MDID_DIR -r $MDID_DIR/requirements.txt mdid_env

## add git autocomplete, git prompt and a few other niceties to the cmd line
## and stick in a .bash-profile to autosource them

cp $PROVISION_DIR/.bash-completion $HOME_DIR
cp $PROVISION_DIR/.git-prompt $HOME_DIR
cp $PROVISION_DIR/.mdid-funcs $HOME_DIR
cp $PROVISION_DIR/.bash_profile $HOME_DIR


#source ~/.profile
#
#if [ -z "$VAR" ] || [ "$VAR" != "value" ]; then
#  echo "export VAR=value" >> ~/.profile
#fi
#
#if [ $(pwd) != "/vagrant" ]; then
#  echo "cd /vagrant" >> ~/.profile
#fi


# create a virtual environment (if needed)
#[[ ! -d venv.vagrant/ ]] && virtualenv venv.vagrant

# enter our virtual environment
#source venv.vagrant/bin/activate


# move into our project dir
cd $MDID_DIR

# install our requirements
pip install --upgrade -r requirements.txt

##############################################################################
# Configure MDID
##############################################################################
# create the MDID database
mysql -uroot -pmdid < .vagrant_provision/create_database.sql

# create the local settings
if [ -f $CONFIG_DIR/settings_local.py ]; then
  # backup any existing local settings first
  mv $CONFIG_DIR/settings_local.py $ROOIBOS_DIR/settings_local.backup.py
fi
# Get the default gateway IP address so we can add it to INTERNAL_IPS
GATEWAY_IP=`route -n | grep 'UG' | awk '{print $2}'`
# filter our local settings template, replacing necessary values
cat $PROVISION_DIR/settings_local.vagrant.py \
  | sed -e "s/<<GATEWAY_IP>>/$GATEWAY_IP/" \
  > $ROOIBOS_DIR/settings_local.py

# move into the $MDID directory (django 1.6 now has manage.py in the top dir)
cd $MDID_DIR
# make manage.py executable like "./mangage.py syncdb"
chmod +x manage.py

# setup the database
python manage.py syncdb --noinput
python manage.py createcachetable cache


echo -e "################# Adding Upstart scripts for Solr and the Workers #################"
cp $PROVISION_DIR/mdid3-*.conf /etc/init


## make sure settings_local (if it exists) is not copied over
# rm

echo -e "################# Starting Up Services #################"
# start up the services
service mdid3-solr start
service mdid3-workers start
