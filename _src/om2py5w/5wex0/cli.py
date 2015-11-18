# -*- coding: utf-8 -*-

import requests

def main():
	print "input your diary:"
	while True:
		input = raw_input(">>> ")
		if input in ['q']:
			return
		else:
			write(input)
			
def write(line):
	text = {"newline": line, "save":"save"}
	requests.get('http://faketooth.sinaapp.com/new_diary', params = text)
	
	
if __name__ == '__main__':
	main()