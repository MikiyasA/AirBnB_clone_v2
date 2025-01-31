#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
apt-get -y update
apt-get -y install nginx
service nginx start
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
fake_html="<html>
  <head>
  </head>
  <body>
    ALX School
  </body>
</html>"
#touch /data/web_static/releases/test/index.html
echo "$fake_html" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default
service nginx restart
exit 0
