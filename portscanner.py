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

for i in range(1, 65535):
	isOpen(ip, i)
