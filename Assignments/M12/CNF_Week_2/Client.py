import socket
import threading

def datareceived(server):
	while  True:
		data = server.recv(1024)
		data = data.decode()
		server.send(data.encode())
		
def main():
	host = '127.0.0.1'
	port = 5000
	s = socket.socket()
	s.connect((host, port))
	threading.Thread(target = datareceived, args = (server,).start())
	while True:
		message = input("Enter the field: ")
		server.send((message).encode())
	server.close()

if __name__ == '__main__':
	main()