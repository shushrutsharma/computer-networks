import socket
import os
import select
import tqdm

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step
host = "" # the ip address or hostname of the server, the receiver
port = 5001 # the port, let's use 5001
s = socket.socket()
print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")

def file_transfer_ts():
    path = input("Enter the File path : ")
    # the name of file we want to send, make sure it exists
    filename = input("Enter File name : ")
    # get the file size
    filesize = os.path.getsize(path+filename)
    # send the filename and filesize
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())

    # start sending the file
    with open(path+filename, "rb") as f:
        for _ in range(filesize//BUFFER_SIZE + 1):
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            s.sendall(bytes_read)
        f.close()
    for _ in tqdm.tqdm(range(filesize)):
        pass
    print("[+] File transfer completed. ")
    return None

def file_transfer_tc():
    # receive the file infos
    # receive using client socket, not server socket
    received = s.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    # remove absolute path if there is
    filename = os.path.basename(filename)
    # convert to integer
    filesize = int(filesize)

    # start receiving the file from the socket
    # and writing to the file stream
    with open(filename, "wb") as f:
        for _ in range(filesize//BUFFER_SIZE + 1):
            # read 1024 bytes from the socket (receive)
            bytes_read = s.recv(BUFFER_SIZE)
            if not bytes_read:    
                break
            # write to the file the bytes we just received
            f.write(bytes_read)
        f.close()
    for _ in tqdm.tqdm(range(filesize)):
        pass
    print("[+] File transfer completed. ")
    return None

while True:
    message_send = input("client >> ")
    s.send(message_send.encode())
    if message_send == "!transfer":
        message_recv = s.recv(BUFFER_SIZE).decode() 
        print("server >>", message_recv)
        message_recv = s.recv(BUFFER_SIZE).decode()
        if message_recv == "!okay":
            file_transfer_ts() 
    elif message_send == "!quit": 
        break
    else:
        message_recv = s.recv(BUFFER_SIZE).decode() 
        print("server >>", message_recv)
        if message_recv == "!transfer":
            s.send("!okay".encode())
            file_transfer_tc()

        
s.close()