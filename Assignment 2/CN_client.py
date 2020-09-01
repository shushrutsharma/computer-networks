import socket
cl=socket.socket()
host=socket.gethostname()
port=6666
cl.connect((host,port))
k=cl.recv(1024).decode()
print(k)
