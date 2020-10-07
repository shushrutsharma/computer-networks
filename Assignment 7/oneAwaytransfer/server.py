import socket
s = socket.socket()
host = socket.gethostname()
port = 5004
s = socket.socket()		
s.bind((host,port))
s.listen(1)
print("Listening .... ")
conn,addr = s.accept()	        
print("Connected to ", addr)

sentence = conn.recv(2048).decode()
print('File requested by Client : ',sentence)

filename = sentence
file = open(filename, 'rb')
file_data = file.read(1024)
conn.send(file_data)
print("Data sent successfully.")

conn.close()