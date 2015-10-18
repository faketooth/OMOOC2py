# -*- coding: utf-8 -*-
'''
http://www.iomooc.com/pages/cards.html?taskId=313a2360-6db3-11e5-a837-0800200c9a66#tip0
'''
import sys
import logging

def readHistory(file):
	try:
		history = open(file, 'rb')
	except IOError:
		print "No history to show..."
		return 
	lines = history.readlines()
	print '='*10+' Start to print the history... '+'='*10
	for line in lines:
		print line,
	print '='*10+' History printing ends. '+'='*10
	history.close()

def appendHistory(file):
	logging.basicConfig(format='%(asctime)-15s %(message)s', filename=file, level=logging.DEBUG)
	print 'Start to log...'
	print 'To stop this script, input "exit" and hit the "ENTER" key.'
	input = raw_input("> ")
	logging.debug(input)
	while(input != 'exit'):		
		input = raw_input("> ")
		logging.debug(input)

