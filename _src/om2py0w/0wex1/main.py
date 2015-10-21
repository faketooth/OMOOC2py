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
	print '='*10+' Start to print the history... '+'='*10
	for line in lines:
		print line,
	print '='*10+' History printing ends. '+'='*10
	history.close()

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

def main(argv):
	file = sys.argv[1] 
	readHistory(file)
	appendHistory(file)

if __name__ == '__main__':
	if(len(sys.argv) > 2):
		usage = 'Run the script like this:\n\tpython main.py <history.log>'
		print usage
		sys.exit(-1)
	if(len(sys.argv) == 1):
		sys.argv.append('history.log')
	main(sys.argv)	
