# server.py
import socket
import time
import datetime
import tqdm
from time import sleep
import sys
from datetime import timedelta
import os
from _thread import *
# create a socket object
s = socket.socket()

#Word display function
def typewritter(msg):
        for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.05)


def close():
        s.shutdown(socket.SHUT_RDWR)
        s.close()
        print("Server close")

typewritter("[+] Socket successfully created\n")
# get local machine name
host = socket.gethostname()
port = 8888
ThreadCount = 0
# bind to the port
s.bind((host,port))
typewritter("[+] Socket is binded to "+str(port)+"\n")
# queue up to 5 requests
s.listen(5)
typewritter("[+] Socket is listening\n")
#Waiting for connection from client
typewritter("[+] Socket is waiting connection from client\n")
def threaded_client(connection):
        typewritter("[+] Connetion establish \n")
        while True:
                # establish a connection
                sel = connection.recv(1024).decode('utf-8')
                if sel == '1':
                        ctime=datetime.datetime.now().strftime('%A %d %B %Y %H:%M:%S %p')
                        connection.send(str(ctime).encode())
                elif sel == '2':
                        ytime=datetime.datetime.now() - datetime.timedelta(days = 1)
                        connection.send(str(ytime.strftime('%A %d %B %Y')).encode())
                elif sel == '3':
                        Ttime = datetime.datetime.now() + datetime.timedelta(days = 1)
                        connection.send(str(Ttime.strftime('%A %d %B %Y')).encode())
                elif sel == '0':
                        close()
        connection.close()
#Main
while True:
        client,addr = s.accept()
        print('Connected to :'+addr[0]+':'+str(addr[1]))
        start_new_thread(threaded_client,(client,))
        ThreadCount += 1
        print('Thread Number:' + str(ThreadCount))
s.close()



