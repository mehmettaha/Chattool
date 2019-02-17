import socket
import threading as th

ADDRESS = socket.gethostbyname(socket.gethostname())
PORT = 3

def receive_thread(sock):
    try:
        message = sock.recv(1000, 0)
        print(message.decode("utf-8"))
    except ConnectionResetError:
        return None
        
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    try:
        sock.connect((ADDRESS,PORT))
        th._start_new_thread(receive_thread, (sock,))
        msg = ""
        while msg != "exit":
            try:
                sock.send(input("").encode("utf-8"))
            except ConnectionResetError:
                print("Connection lost while sending message")
                break
    except ConnectionRefusedError:
        print("Server not running")
        pass

    
  
       
    
    