#!/bin/bash

openssl genrsa -out private.pem 2048 && \ 
openssl rsa -in private.pem -outform PEM -pubout -out sessionPub.pem \
&& openssl rsa -in private.pem -out sessionPriv.pem -outform PEM && \
rm private.pem && \
openssl req -newkey rsa:2048 -nodes -keyout web.key -x509 -days 365 -out web.cert -subj "/C=GB/ST=London/L=London/O=jimi/OU=jimi/CN=jimiproject"