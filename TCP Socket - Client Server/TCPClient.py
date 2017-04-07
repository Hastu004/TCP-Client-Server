from socket import *
from sys import *

serverName = 'localhost'

serverPort = 12000

clientSocket = socket(AF_INET,SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

sentence = input('Ingrese el primer dígito para la suma.')

clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(1024)

print ('From Server:'), modifiedSentence

clientSocket.close()

