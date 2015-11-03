# -*- coding: utf-8 -*-

import socket

def main():
	clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	welcome = 'Welcome to use this net-diary. Please input your name:\n>>> '
	username = raw_input(welcome)
	while not username:
		username = raw_input(welcome)
	print "Hello, %s! " % (username)
	print "q/quit/exit for quit."
	print "history/r for history diary."
	print "hit Enter-key to send the message."
	while True:
		input = raw_input(">>> ")
		if input in ['q', 'quit', 'exit']:
			quit(clientSock)
			break
		if input in ['']:
			print "Empty Message won't send!"
			continue
		if input in ['history', 'r']:
			history()
			continue
		clientSock.sendto(input, ('localhost', 9527))
	print "Bye~~"

def quit(clientSock):		
	clientSock.close()
	
def history():
	print "Okey. Here is your history diary..."
	
if __name__ == '__main__':
	main()