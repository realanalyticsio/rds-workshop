#!/bin/bash

apt-get update
apt-get install -y dos2unix

# fix line endings
dos2unix /vagrant/start-jupyter.sh
