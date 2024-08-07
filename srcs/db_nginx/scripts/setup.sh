#!/bin/bash

chown -R postgres:postgres /var/lib/postgresql/15/main
chown -R postgres:postgres /etc/postgresql/15/main
chown -R postgres:postgres /var/log/postgresql
service postgresql start 
echo "---------------------------------------------------->$DB_USER"
echo "---------------------------------------------------->$DB_NAME"
psql -U $DB_USER -c "drop database $DB_NAME;"
psql -U $DB_USER -c "create database $DB_NAME;"
echo "---------------------------------------------------->"
psql -U $DB_USER -c "alter user $DB_USER with password '${DB_PASS}'"
echo "---------------------------------------------------->"

cat << EOF > /etc/nginx/nginx.conf
user www-data;
worker_processes auto;
pid /run/nginx.pid;
error_log /var/log/nginx/error.log;
events {}

http {
    include       /etc/nginx/mime.types;
    server {
        listen 443 ssl;
        server_name localhost;

        ssl_certificate $PATH_CRT/my.crt;
        ssl_certificate_key $PATH_CRT/my.key;
        location / {
            root  /usr/share/nginx/html;
            index home.html;
        }
        location /api {
            proxy_pass http://$AUTH_SERVER:8000;
            proxy_set_header Host \$host;
            proxy_set_header X-Real-IP \$remote_addr;
            proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto \$scheme;
        }
    }
    server {
        listen 80;
        server_name localhost;

        location / {
            return 301 https://\$host\$request_uri;
        }
    }
}
EOF
touch /is_ready/yes
nginx -g "daemon off;"
