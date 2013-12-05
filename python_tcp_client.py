import sys
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((sys.argv[1], int(sys.argv[2])))

sock.send(b'hello from tcp client')
data, addr = sock.recvfrom(1024)
print( "ECHOed", data, addr)
sock.close()

