# server.py
import socket
import time
import datetime
import tqdm
from time import sleep
import sys
from datetime import timedelta
# create a socket object
serversocket = socket.socket()

#Word display function
def typewritter(msg):
        for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.05)

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
        typewritter("[+] Connetion establish\n")
	while True:
                sel = clientsocket.recv(1024).decode('utf-8')
                if sel == '1':
                        ctime=datetime.datetime.now().strftime('%A %d %B %Y %H:%M:%S %p')
                        clientsocket.send(str(ctime).encode())
                elif sel == '2':
                        ytime=datetime.datetime.now() - datetime.timedelta(days = 1)
                        clientsocket.send(str(ytime.strftime('%A %d %B %Y')).encode())
                elif sel == '3':
                        Ttime = datetime.datetime.now() + datetime.timedelta(days = 1)
                        clientsocket.send(str(Ttime.strftime('%A %d %B %Y')).encode())
                elif sel == '0':
                        clientsocket.close()
        clientsocket.close()
clientsocket.close()
