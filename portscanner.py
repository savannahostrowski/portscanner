#Port Scanner - Enter an IP address and a port range where the program will then attempt to find open ports on the given computer by connecting to each of them. On any successful connections mark the port as open.

import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)


def isOpen(ip, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect((ip, int(port)))
		s.shutdown(2)
		print(str(port) + ': ' + 'Open')
	except:
		print(str(port) + ': ' + 'Closed')

isOpen(ip, 8000)

# for i in range(1, 65535):
# 	isOpen(ip, i)