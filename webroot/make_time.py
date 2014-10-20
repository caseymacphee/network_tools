#!/usr/bin/env python

"""
make_time.py

simple script that returns and HTML page with the current time
"""

import datetime

def print_time():
	time =  datetime.datetime.now().isoformat()

	print "Someone made a request at : {}".format(time)




