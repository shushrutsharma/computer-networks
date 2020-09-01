import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 12345))
while True:
    my = input("client: ")
    s.send(bytes(my, "utf-8"))
    if my == "exit":
        break
    msg = s.recv(1024)
    print("server: ", msg.decode("utf-8"))