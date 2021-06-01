#!/bin/bash

source .venv/bin/activate
gunicorn --bind 0.0.0.0:4443 --workers 4 --threads 10 --certfile=data/web.cert --key=data/web.key start