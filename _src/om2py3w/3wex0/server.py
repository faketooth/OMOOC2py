# -*- coding: utf-8 -*-

import socket
import select
import logging 

logging.basicConfig(format='%(asctime)-15s|%(message)s', filename='history.log', level=logging.DEBUG)

def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind(('', 9527))
	his_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	his_sock.bind(('', 9528))
	his_sock.listen(5)
	
	while True:
		reads, wirtes, errs = select.select([sock,his_sock,],[],[],3)
		print len(reads)
		if len(reads) != 0:
			data, (host, port) = sock.recvfrom(8192)
			user, message = data.split(": ")
			if message in ['r', 'history']:
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
	lines = ['a', 'b', 'c', 'd']
	for line in lines:
		conn.sendall(line)
		print 'wtf'
	conn.sendall('EOT')
	conn.close()

if __name__ == '__main__':
	main()	