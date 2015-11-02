# -*- coding: utf-8 -*-

import socket

def main():
	clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	while True:
		input = raw_input(">>> ")
		if input in ['q', 'quit', 'exit']:
			break
		clientSock.sendto(input, ('localhost', 9527))
		
	clientSock.close()
	
if __name__ == '__main__':
	main()