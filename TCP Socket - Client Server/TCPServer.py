from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('localhost',serverPort))

serverSocket.listen(1)

print ('The server is ready to receive')

while 1:
	
	connectionSocket, addr = serverSocket.accept()
	
	digito1 = connectionSocket.recv(1024)
	
	total = digito1
	
	connectionSocket.send(total.encode())
	
	connectionSocket.close()
	
	
	
