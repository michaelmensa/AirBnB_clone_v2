#!/usr/bin/env bash
#Bash script to set up web servers for deployment of web_static

#install Nginx if not exist
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

# create directories
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test

#create index.html in /PATH/
sudo touch /data/web_static/releases/test/index.html

#echo into index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

#create symbolic link to /PATH
sudo ln -s -f /data/web_static/releases/test /data/web_static/current

#change owner
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location/hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

#restart nginx
sudo service nginx restart
