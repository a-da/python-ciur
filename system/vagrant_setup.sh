#!/usr/bin/env bash
# description: provision script for vagrant
# command: vagrant up

# to mongo repository OPTIONAL
#if ls /etc/apt/sources.list.d/mongodb.list &>> /dev/null
#    then
#        echo "already added mongo repository"
#    else
#        sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
#        echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list
#fi

sudo apt-get -y update
sudo apt-get install -y $(cat /vagrant/packages.txt | grep -oP "^[^#\s]+")

#install virtualenv
sudo pip install --upgrade pip virtualenv
sudo mkdir /opt/python-virtualenv/
sudo virtualenv /opt/python-virtualenv/alfa
#sudo /opt/python-virtualenv/alfa/bin/pip install /vagrant