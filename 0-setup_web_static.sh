#!/usr/bin/env bash
# Bash script to set up web server
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo service nginx start
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo echo "Holberton School" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu /data
sudo chgrp -R ubuntu /data
sudo sed -i '/listen 80 default_server;/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
sudo service nginx restart
