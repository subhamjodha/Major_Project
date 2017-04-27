import socket
import struct

HOST = socket.gethostbyname(socket.gethostname()) #"localhost"
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print "SERVER Running At %s :" %(HOST)


while True:
    client, address = s.accept()
    print "Got connection from",address
    buf = ''
    while len(buf) < 4:
        buf += client.recv(4 - len(buf))
    size = struct.unpack('!i', buf)[0]
    print size
    with open('temp.apk', 'wb') as f:
        while size > 0:
            data = client.recv(4096)
            f.write(data)
            size -= len(data)
    print('APK Saved')
    client.sendall('APK Received')
    client.close()