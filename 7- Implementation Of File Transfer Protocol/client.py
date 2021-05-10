import socket                 
s = socket.socket()          
port = 12345                
s.connect(('127.0.0.1', port)) 

path = input("Path : ") 

print("Processes : \n 1) quit \n 2) print \n 3) transfer_tc \n 4) transfer_ts ")

while True:
    command = input("Enter the process : ")
    if command == "quit":
        break
    elif command == "print":
        filename = input("Enter the name of file being read : ")
        doc = open(path+filename,'r')
        print(doc.read())
    elif command == "transfer_tc": 
        filename = input("Enter the name of file being transfered : ")
        doc = open(path+filename,'ab')
        doc_data = s.recv(1024)
        doc.write(doc_data)
        print("File has been received successfully...")
    elif command == "transfer_ts":
        filename = input("Input the name of the file: ")
        doc = open(path+filename,'rb')
        doc_data = doc.read(1024)
        s.send(doc_data)
        print("Data has been sent....")

s.close()
