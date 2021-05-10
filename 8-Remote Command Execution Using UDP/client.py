import socket
import os
cl = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("192.168.1.2", 6789)
cl.sendto("Connection established".encode(), addr)
while True:
    x = input("Enter the command: ")
    cl.sendto(x.encode(), addr)
    y = cl.recvfrom(1024)
    print("Server's output : ", y[0].decode())