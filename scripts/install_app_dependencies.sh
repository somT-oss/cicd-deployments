#!/bin/bash
sudo pip3 install virtualenv
cd /home/ubuntu/cicd-deployments/
virtualenv env
source env/bin/activate
sudo pip3 install -r requirements.txt