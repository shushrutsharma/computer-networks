import socket
s=socket.socket()
print("socket created")
host=socket.gethostname()
port=6666
s.bind((host,port))
s.listen(11)
print("waiting")
while True:
    cl,addr=s.accept()
    print("connected with client",addr)
    command=input("enter command:")
    cl.send(bytes(command,'utf-8'))
    cl.close()
