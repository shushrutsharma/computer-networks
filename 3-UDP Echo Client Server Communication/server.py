import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(("127.0.0.1", 10000))

while 1:
    bytesAddressPair = s.recvfrom(1024)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    
    print("WE GOT A MESSAGE!!: ", message)

    
    a = input("WHAT DO YOU WANT TO SAY?? : ")
    s.sendto(str(a).encode(), address)