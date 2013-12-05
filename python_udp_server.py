import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 5555))

while True:
	data, addr = sock.recvfrom(1024)
	print(data, addr)
	sock.sentto(b'ECHO '+data, addr)
