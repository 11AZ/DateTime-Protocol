# server.py
import socket
import time
import datetime
import tqdm
from time import sleep
import sys
# create a socket object
serversocket = socket.socket()

#Word display function
def typewritter(msg):
	for char in msg:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.1)

typewritter("[+] Socket successfully created\n")
# get local machine name
host = socket.gethostname()
port = 8888
# bind to the port
serversocket.bind((host,port))
typewritter("[+] Socket is binded to "+str(port)+"\n")
# queue up to 5 requests
serversocket.listen(5)
typewritter("[+] Socket is listening\n")
#Waiting for connection from client
typewritter("[+] Socket is waiting connection from client\n")
while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()
    clientsocket.send(bytes('Welcome to the server', 'utf-8'))
    typewritter('Got a connection from %s' % str(addr))
    currentTime = datetime.datetime.now()
    clientsocket.send(str(currentTime).encode())
    clientsocket.close()
