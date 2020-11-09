import socket
from threading import Thread

def thread():
	while True:
		data = conn.recv(1024)
		print('Client Request :' + data.decode())
		if data == 'quit' or not data:
			print("Server Exiting")
			break  
		data = input('Server Response:')
		conn.sendall(data.encode())  

host = socket.gethostname()
port = 1027
s = socket.socket()		
s.bind((host,port))
s.listen(5)

print("Waiting for clients...")
while True:
	conn,addr = s.accept()	        
	print("Connected by ", addr)
	pr = Thread(target=thread)
	pr.start()

conn.close()
