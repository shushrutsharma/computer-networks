import socket
import threading
import sys

FLAG = False

def recv_from_client(conn):
    global FLAG
    try:
        while True:
            if FLAG == True:
                break
            message = conn.recv(1024).decode()

            if message == 'quit':
                conn.send('quit'.encode())
                conn.close()
                print('Connection Closed')
                FLAG = True
                break
            print('Client: ' + message)
    except:
        conn.close()

def send_to_client(conn):
    global FLAG
    try:
        while True:
            if FLAG == True:
                break
            send_msg = input('')
            if send_msg == 'quit':
                conn.send('quit'.encode())
                conn.close()
                print('Connection Closed')
                FLAG = True
                break
            conn.send(send_msg.encode())
    except:
        conn.close()

def main():
    threads = []
    global FLAG

    HOST = 'localhost'
    serverPort = 6500

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serverSocket.bind((HOST, serverPort))
    print("Socket binded.")

    serverSocket.listen(1)
    print("Listening.....")

    connectionSocket, addr = serverSocket.accept()
    print('Connection Established with a Client on ', addr, '\n')

    t_rcv = threading.Thread(target=recv_from_client, args=(connectionSocket,))
    t_send = threading.Thread(target=send_to_client, args=(connectionSocket,))

    threads.append(t_rcv)
    threads.append(t_send)
    t_rcv.start()
    t_send.start()

    t_rcv.join()
    t_send.join()

    print('EXITING')
    serverSocket.close()

    sys.exit()

if __name__ == '__main__':
    main()