import socket
import threading as th
import time

ADDRESS = socket.gethostbyname(socket.gethostname())
POR = 3

clientlist = {}

def client_thread(conn : socket):
    while True:
        try :
            message = conn.recv(1000)
        except ConnectionRefusedError:
            return None
        print("Client on port %s:%s says : %s"%(clientlist[conn][0],clientlist[conn][1],message.decode("utf-8")))

def accept_thread(sock):
    while True:
        conn, addr = sock.accept()
        ip = addr[0] 
        port = addr[1]
        print("Connected by %s on port %d"% (ip, port))
        clientlist[conn] = ip, port
        th._start_new_thread(client_thread, (conn,))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    print("Welcome to the server")
    sock.bind((ADDRESS, POR))
    sock.listen()
    print("Listening on",POR)

    th._start_new_thread(accept_thread, (sock,))
    input("Press enter to quit any time\n")
    
    

