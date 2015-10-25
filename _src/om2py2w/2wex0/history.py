# -*- coding: utf-8 -*-

import sys
import logging

def readHistory(file):
	try:
		history = open(file, 'rb')
	except IOError:
		print "No history to show..."
		return 
	lines = history.readlines()
	history.close()
	return lines

def appendHistory(file):
	logging.basicConfig(format='%(asctime)-15s %(message)s', filename=file, level=logging.DEBUG)
	print 'Start to log...'
	print 'To stop this script, input "exit" and hit the "ENTER" key.'
	print '"history" command will print all history log.'
	input = raw_input("> ")
	while(input != 'exit'):
		logging.debug(input)
		if(input == 'history'):
			readHistory(file)		
		input = raw_input("> ")

#lines = readHistory('history.log')
#print lines