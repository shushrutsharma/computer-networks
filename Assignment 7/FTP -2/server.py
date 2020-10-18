import socket
import os
import select
import tqdm
# device's IP address
SERVER_HOST = ""
SERVER_PORT = 5001
# receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"
s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
client_socket, address = s.accept() 
print(f"[+] {address} is connected.")

def file_transfer_ts():
    # receive the file infos
    # receive using client socket, not server socket
    received = client_socket.recv(BUFFER_SIZE).decode()
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
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:    
                break
            # write to the file the bytes we just received
            f.write(bytes_read)
        f.close()
    for _ in tqdm.tqdm(range(filesize)):
        pass
    print("[+] File transfer completed. ")
    return None

def file_transfer_tc():
    path = input("Enter the File path : ")
    # the name of file we want to send, make sure it exists
    filename = input("Enter File name : ")
    # get the file size
    filesize = os.path.getsize(path+filename)
    # send the filename and filesize
    client_socket.send(f"{filename}{SEPARATOR}{filesize}".encode())

    # start sending the file
    with open(path+filename, "rb") as f:
        for _ in range(filesize//BUFFER_SIZE + 1):
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            client_socket.sendall(bytes_read)
        f.close()
    for _ in tqdm.tqdm(range(filesize)):
        pass
    print("[+] File transfer completed. ")
    return None

while True:
    message_send = input("server >> ")
    client_socket.send(message_send.encode())
    if message_send == "!transfer":
        message_recv = client_socket.recv(BUFFER_SIZE).decode()
        print("client >>", message_recv)
        message_recv = client_socket.recv(BUFFER_SIZE).decode()
        if message_recv == "!okay":
            file_transfer_tc()
    elif message_send == "!quit":
        break
    else:
        message_recv = client_socket.recv(BUFFER_SIZE).decode() 
        print("client >>", message_recv)
        if message_recv == "!transfer":
            client_socket.send("!okay".encode())
            file_transfer_ts()

        


client_socket.close() # close the client socket
s.close() # close the server socket
