#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir /data/ 
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/

echo -e "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '33i \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-enabled/default
sudo service nginx restart
