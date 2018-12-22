import socket
import threading
import csv
roll_numbers = []
def server(connection):
    while True:
        data = connection.recv(1024)
        data = data.decode()

def main():
    host = '127.0.0.1'
    port = 5000
    s = socket.socket()
    connections = int(input('users'))
#host = str(socket.gethostbyname(socket.gethostname()))
    s.bind((host, port))
    s.listen(10)
    for connection in connections:
        c, addr = s.accept()
        print("Connection is established with" + str(addr))
        clients.append(c)
        thread = threading.Thread(target = server, args = (c, addr)).start()
        thread.start()
    s.close()
    
if __name__ == '__main__':
        main()
