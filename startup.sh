#!/bin/bash 

sudo apt update 
sudo apt-get install python3-venv 

sudo python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

sudo mkdir /opt/book-donation-app-1-2
sudo chown -R jenkins /opt/book-donation-app-1-2

sudo systemctl daemon-reload
sudo systemctl stop app.service
sudo systemctl start app.service