import socket
import threading
import sys

FLAG = False

def send_to_server(clsock):
    global FLAG
    while True:
        if FLAG == True:
            break
        send_msg = input('')
        clsock.sendall(send_msg.encode())


def recv_from_server(clsock):
    global FLAG
    while True:
        data = clsock.recv(1024).decode()
        if data == 'quit':
            print('Closing connection')
            FLAG = True
            break
        print('Server: ' + data)

# this is main function
def main():
    threads = []
    HOST = 'localhost'
    PORT = 6500

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    clientSocket.connect((HOST, PORT))
    print('Client is connected to the Server\n')
    
    t_send = threading.Thread(target=send_to_server, args=(clientSocket,))

    t_rcv = threading.Thread(target=recv_from_server, args=(clientSocket,))

    threads.append(t_send)
    threads.append(t_rcv)
    t_send.start()
    t_rcv.start()

    t_send.join()
    t_rcv.join()

    print('EXITING')
    sys.exit()

if __name__ == '__main__':
    main()