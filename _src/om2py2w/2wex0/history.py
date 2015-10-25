# -*- coding: utf-8 -*-

import sys
import logging

def readHistory(file):
	try:
		history = open(file, 'rb')
	except IOError:
		print "No history to show..."
		return []
	lines = history.readlines()
	history.close()
	return lines

def appendHistory(file, line):
	logging.basicConfig(format='%(message)s', filename=file, level=logging.DEBUG)
	logging.debug(line)
	print line

#lines = readHistory('history.log')
#print lines