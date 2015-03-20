#!/usr/bin/env bash
HOME_DIR=`pwd`
VAGRANT_DIR=/vagrant
PROVISION_DIR=$VAGRANT_DIR/.vagrant_provision
MDID_DIR=$HOME_DIR/mdid
MDID_DATA_DIR=$HOME_DIR/mdid-data
CONFIG_DIR=$MDID_DIR/config
ROOIBOS_DIR=$MDID_DIR/rooibos

sudo -u vagrant mkdir bootstrap_logs

##############################################################################
# A Vagrant provisioning shell script to setup an MDID Development VM
##############################################################################
# add ppa for ffmpeg
add-apt-repository ppa:mc3man/trusty-media

# Update our apt sources
apt-get update

# Make sure we are starting from an up-to-date system
apt-get upgrade -y
apt-get dist-upgrade -y

##############################################################################
# Install MySQL
##############################################################################
# The mysql-server package interactively prompts for the root pasword to the
# MySQL server.  These commands will cache the password settings, and they
# will be used by the mysql-server package on installation.  Since this is
# pretty insecure anyway, no attempt is made at using a secure password :)
#
# Sets the MySQL root password to 'mdid'
echo mysql-server mysql-server/root_password password mdid | debconf-set-selections
echo mysql-server mysql-server/root_password_again password mdid | debconf-set-selections

# Now we can install the packages
# mysql-server: The MySQL server
# mysql-client: The MySQL client utilities
# libmysqlclient-dev: MySQL developmental libraries, needed to build the python
#   MySQL module
apt-get install -y mysql-server mysql-client libmysqlclient-dev 2>> bootstrap_logs/install_errors.txt

##############################################################################
# Install other dependencies
##############################################################################
# Java is needed to run Solr
apt-get install -y openjdk-7-jre-headless 2>> bootstrap_logs/install_errors.txt

# RabbitMQ is needed to manage the worker jobs
apt-get install -y rabbitmq-server 2>> bootstrap_logs/install_errors.txt

# Memcached is used for django's memory object cache
apt-get install -y memcached 2>> bootstrap_logs/install_errors.txt

##############################################################################
# Python build dependencies
##############################################################################
# Need the python development libs
apt-get install -y python-dev 2>> bootstrap_logs/install_errors.txt

# PyODBC needs the unixodbc libs
apt-get install -y unixodbc unixodbc-dev 2>> bootstrap_logs/install_errors.txt

# python-ldap needs ldap and sasl libraries
apt-get install -y libldap2-dev libsasl2-dev 2>> bootstrap_logs/install_errors.txt

# Pillow needs image libraries
apt-get install -y libtiff5-dev libjpeg8-dev zlib1g-dev 2>> bootstrap_logs/install_errors.txt

# ffmpeg
apt-get install -y ffmpeg 2>> bootstrap_logs/install_errors.txt


##############################################################################
# Setup files and directories
##############################################################################
# create a symlink from /vagrant to our home dir
sudo -u vagrant ln -s $VAGRANT_DIR $MDID_DIR

# create directories for our mdid data
sudo -u vagrant mkdir $MDID_DATA_DIR
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
apt-get install -y python-pip 2>> bootstrap_logs/install_errors.txt

# install virtualenv
pip install -y virtualenv 2>> bootstrap_logs/install_errors.txt
pip install -y virtualenvwrapper 2>> bootstrap_logs/install_errors.txt

# move into our project dir
cd $MDID_DIR

# create a virtual environment (if needed)
[[ ! -d venv.vagrant/ ]] && virtualenv venv.vagrant

# enter our virtual environment
source venv.vagrant/bin/activate

# install our requirements
pip install -r requirements.txt

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

##############################################################################
# Add Upstart scripts for Solr and the Workers
##############################################################################
cp $PROVISION_DIR/mdid3-*.conf /etc/init

## add git autocomplete, git prompt and a few other niceties to the cmd line
## and stick in a .bash-profile to autosource them

cp $PROVISION_DIR/.bash-completion $HOME_DIR
cp $PROVISION_DIR/.git-prompt $HOME_DIR
cp $PROVISION_DIR/.mdid-funcs $HOME_DIR
cp $PROVISION_DIR/.bash-profile $HOME_DIR

## make sure settings_local (if it exists) is not copied over
rm

# start up the services
service mdid3-solr start
service mdid3-workers start
