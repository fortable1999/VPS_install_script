import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 5555))
sock.listen(5)

while True:
    conn, addr = sock.accept()
    print(addr, "Connected")
    data = conn.recv(1024)
    print(data, "Data received")
    conn.close()
