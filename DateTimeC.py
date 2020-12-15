import socket
import sys
from tqdm import tqdm , trange
import datetime
import time
from time import sleep
# create a socket object
s = socket.socket()

# get local server machine name
host = "192.168.0.101"

port = 8888
# connection to hostname on the port.
print(f"[+] Connecting to {host}:{port}")
#Progress bar
pbar = tqdm(total=100)
for i in range(10):
    time.sleep(0.3)
    pbar.update(10)
pbar.close()
s.connect((host, port))
print("[+] connected")
time.sleep(1)
#whle lopp
while True:
	#Front page
	print('-----------------------WELCOME TO THE DATETIME SERVER-----------------------')
	print('1-GO TO DATETIME SERVICE')
	print('bye- TO EXIT THE PROGRAM')
	a = input('Enter selection:')
	print(a)
	#if statement
	if a == '1':
		#Datetime Page
		print('Welcome to the Date time service')
		print('Enter <1> to check today date and time')
		print('Enter <2> to check yesterday date')
		print('Enter <3> to check tommorrow date')
		print('Enter <99> to exit the program')
		date = input('Choose what you want: ')
		if date == '1':
			s.send(date.encode()) #Send date to server
			tm = s.recv(36) #Receive time from server
			print('Today time : %s' % tm.decode('utf-8'))
		elif date == '2':
			s.send(date.encode())
			tmY = s.recv(23) #Receive yesterday date
			print('Yesterday date :%s'% tmY.decode('utf-8'))
		elif date == '3':
			s.send(date.encode())
			tmT = s.recv(23) #Receive tommorow date
			print('Tommorrow date : %s' % tmT.decode('utf-8'))
		else:
			print('No input from server')
	else:
		print('Error')

