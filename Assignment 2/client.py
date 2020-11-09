import socket
s = socket.socket()
host = socket.gethostname()
port = 1027
s.connect((host,port))
s.send(bytes('Shushrut Kumar Requesting','utf-8'))
while True:
    data = s.recv(1024)
    if data == 'quit' or not data:
        print("Quiting")
        break
    else:
        print("Server: ",data.decode())
        msg = input("Client: ")
        s.send(msg.encode())
s.close()
