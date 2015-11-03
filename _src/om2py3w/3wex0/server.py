# -*- coding: utf-8 -*-

import socket
import select
import logging 

logging.basicConfig(format='%(asctime)-15s %(message)s', filename='history.log', level=logging.DEBUG)

def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind(('', 9527))
	while True:
		reads, wirtes, errs = select.select([sock,],[],[],3)
		if len(reads) != 0:
			data, (host, port) = sock.recvfrom(8192)
			print "host %s:%s, said: %s" % (host, port, data)
			logging.debug("host %s:%s, said: %s" % (host, port, data))
		print 'no data.'
		
	sock.close()
	
if __name__ == '__main__':
	main()	