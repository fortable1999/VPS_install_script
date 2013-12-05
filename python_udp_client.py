import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(5)
sock.bind(('', 5555))
sock.sendto(b'hello', ('ouroborothon.com', 5555))
data, addr = sock.recvfrom(1024)
print( "ECHOed", data, addr)

