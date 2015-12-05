#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/lunch_app/")

from lunch_app import app as application
application.secret_key = 'secretkey12345'
