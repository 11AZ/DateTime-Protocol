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
	#Receive input from client
	tm = clientsocket.recv(1024)
	print(tm.decode('utf-8'))
	a = tm.decode('utf-8')
	if a == '1':
		currentTime=datetime.datetime.now().strftime("%A %d %B %Y %H:%M:%S %p")
		clientsocket.send(str(currentTime).encode())
		clientsocket.close()
	elif a == '2':
		yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
		clientsocket.send(str(yesterday.strftime('%A %d %B %Y')).encode())
		clientsocket.close()
	elif a == '3':
		tomor = datetime.datetime.now() + datetime.timedelta(days = 1)
		clientsocket.send(str(tomor.strftime('%A %d %B %Y')).encode())
		clientsocket.close()
	else:
		print('Input error')

