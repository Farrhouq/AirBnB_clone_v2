#!/usr/bin/env bash
# This script is used to set up the airbnb clone static page

# check if nginx is installed
sudo su
apt-get update -y
apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared

index="/data/web_static/releases/test/index.html"
touch $index
echo "<html>
  <head>
  </head>
  <body>
   Farrhouqbnb
  </body>
</html>" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root /var/www/html;
    index index.html;
    
    location /hbnb_static {
        alias /data/web_static/current;
	autoindex off;
    }
    location /redirect_me {
        return 301 https://youtube.com;
    }
    error_page 404 /custom_404.html;
    location /404 {
        root /var/www/html;
	internal;
    }
}" > /etc/nginx/sites-available/default

service nginx restart
