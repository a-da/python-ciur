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

VAGRANT_URL=https://dl.bintray.com/mitchellh/vagrant/vagrant_1.7.4_x86_64.deb
VIRTUALBOX_URL=http://download.virtualbox.org/virtualbox/5.0.4/VirtualBox-5.0.4-102546-Linux_amd64.run

function install_vagrant {
    vagrant --help &> /dev/null || (
    echo "[INFO] vagrant not installed, installing it ..."
    gdebi --help &> /dev/null || sudo apt-get update && sudo apt-get install -y gdebi
    wget -nc "${VAGRANT_URL}"
    sudo gdebi --non-interactive vagrant_*.deb
    ) && echo "[INFO] vagrant is installed"
}

function install_virtualbox {
    virtualbox --help &> /dev/null || (
    echo "[INFO] virtualbox not installed, installing it ..."
    wget -nc "${VIRTUALBOX_URL}"
    sudo chmod +x VirtualBox-*.run
    sudo ./VirtualBox-*.run
    ) && echo "[INFO] virtualbox is installed"
}

function install_virtualenv {
    apt-get -y update
    apt-get install -y $(cat packages.txt | grep -oP "^[^#\s]+")
    #install virtualenv
    pip install --upgrade pip virtualenv
    virtualenv /opt/python-env/ciur
    /opt/python-env/ciur/bin/pip install --upgrade -r requirements-pip.txt
}

case "${#}" in
     0)
        echo "[ERROR] Not implemented yet" 1>&2
        ;;
     1)
        ${1}
        ;;
     *)
        echo "[ERROR] This script CAN NOT accept more than one arg" 1>&2
        ;;
esac

