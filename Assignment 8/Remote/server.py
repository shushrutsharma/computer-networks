import socket
import os
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 8000))
print(s.recvfrom(1024)[0].decode())
while True:
    x = s.recvfrom(1024)
    if (x[0].decode() == "stop"):
        break
    ops = os.popen(x[0].decode())
    op = ops.read()
    print(op)
    s.sendto(op.encode(), x[1])
