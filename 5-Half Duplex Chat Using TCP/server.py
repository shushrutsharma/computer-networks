import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 12345))
s.listen(5)
while 1:
    cs, add = s.accept()
    print(f"connection from {add} has been established")
    val = "hi There"
    while val != "exit":
        val = input("server : ")
        cs.send(bytes(val, "utf-8"))
        msg = cs.recv(1024)
        print("client: " + msg.decode("utf-8"))