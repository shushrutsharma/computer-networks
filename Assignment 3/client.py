import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

recv_msg = ""


while recv_msg != "exit":
    a = input("Shushrut, do you want to say something?? : ")
    s.sendto(str.encode(a), ("127.0.0.1", 10000))
    recv_msg = s.recvfrom(1024)
    print("Shushrut, you've got a new message!!:", recv_msg[0])