import socket                
  
s = socket.socket()          
print ("Socket successfully created")

port = 12345                
s.bind(('127.0.0.1', port))         
print ("socket binded to %s" ,port)
s.listen(5)      
print ("socket is listening")            

c, addr = s.accept()      
print('Got connection from', addr)

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
        filename = input("Input the name of the file: ")
        doc = open(path+filename,'rb')
        doc_data = doc.read(1024)
        c.send(doc_data)
        print("Data has been sent....")
    elif command == "transfer_ts":
        filename = input("Enter the name of file being transfered : ")
        doc = open(path+filename,'ab')
        doc_data = c.recv(1024)
        doc.write(doc_data)
        print("File has been received succesfully...")

s.close()