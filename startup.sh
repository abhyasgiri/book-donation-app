#!/bin/bash 

sudo apt update 
sudo apt-get install python3-venv 

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
#python3 -m pip install flask
#python3 -m pip install flask_sqlalchemy
#python3 -m pip install flask_wtf

sudo mkdir /opt/todo-list-app
sudo chown -R jenkins /opt/todo-list-app

sudo systemctl daemon-reload
sudo systemctl stop app.service
sudo systemctl start app.service #need to make the service file 