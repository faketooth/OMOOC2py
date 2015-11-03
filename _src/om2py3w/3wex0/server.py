# -*- coding: utf-8 -*-

import socket
import select
import logging 

logging.basicConfig(format='%(asctime)-15s | %(message)s', filename='history.log', level=logging.DEBUG)

def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind(('', 9527))
	his_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	his_sock.bind(('', 9528))
	his_sock.listen(5)
	
	while True:
		reads, wirtes, errs = select.select([sock,his_sock,],[],[],3)
		if len(reads) != 0:
			data, (host, port) = sock.recvfrom(8192)
			user, message = data.split(": ")
			if message in ['r', 'history']:
				print "Sending history to %s@%s:%s" % (user, host, port)
				sendHistory(his_sock)
				continue
			print "%s@%s:%s, said: %s" % (user, host, port, message)
			logging.debug("%s@%s:%s, said: %s" % (user, host, port, message))
		#print 'no data...'
		
	sock.close()

def sendHistory(his):
	#data = his.recvfrom(1024)
	#print data
	conn, addr = his.accept()
	conn.recv(1024)
	with open('history.log') as history:
		for line in history:
			conn.sendall(line)
			conn.recv(1024)
	conn.sendall('EOT')
	conn.close()

if __name__ == '__main__':
	main()	