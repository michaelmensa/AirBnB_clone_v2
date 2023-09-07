#!/usr/bin/env bash
#Bash script to set up web servers for deployment of web_static.

#install Nginx if not exist
sudo apt-get update
if ! command -v nginx &> /dev/null; then
    echo "Nginx is not installed, installing now..."
    sudo apt-get -y install nginx
    echo "Nginx successfully installed"
else
    echo "Nginx is already installed"
fi

sudo service nginx start

# create directories
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

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
sudo ln -sf /data/web_static/releases/test /data/web_static/current

#change owner
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i "s|server_name _;|server_name _;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tindex index.html;\n\t}\n|" /etc/nginx/sites-available/default

sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
#sudo sed -i '/listen 80 default_server/a location/hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

#restart nginx
sudo service nginx restart
