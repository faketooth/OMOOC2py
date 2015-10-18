# -*- coding: utf-8 -*-
'''

'''
from main import *

def main(argv):
	file = sys.argv[1] 
	readHistory(file)
	appendHistory(file)

if __name__ == '__main__':
	if(len(sys.argv) != 2):
		usage = 'Run the script like this:\n\tpython main.py <history.log>'
		print usage
		sys.exit(-1)
	main(sys.argv)	
