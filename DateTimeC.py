import socket
import sys
from tqdm import tqdm , trange
import datetime
import time
from time import sleep
import os
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

#Front page function
def fmenu():
	print("-------------------------------WELCOME TO DATETIME PROGRAM-------------------------")
	print("|1| Go to date time program")
	print("|0| Exit the program")
	opt = input("Enter your selection:")

	return opt
#Date tiem menu
def Datetime():
	print("This is a simple date time server")
	print("[1] To check for today date and time")
	print("[2] To check for yesterday date")
	print("[3] To check for tommorrow date")
	print("[0] to exit the program")
	sel = input("enter selectij")

	return sel
#Main
while True:
	opt = fmenu()
	loop = 1
	while loop == 1:
		if opt == '1':
			os.system('clear')
			sel = Datetime()
			if sel == '1':
				os.system('clear')
				s.send(sel.encode())
				tm = s.recv(38)
				print("Time and date is %s" % tm.decode('utf-8'))
				a= input("Enter 1")
				if a == '1':
					loop = 1
				else:
					sys.exit()
			elif sel == '2':
				os.system('clear')
				s.send(sel.encode())
				tm = s.recv(38)
				print("Time and date is %s" % tm.decode('utf-8'))
				a = input("enter 1 to back||Enter 0 to exit")
				if a == '1':
					loop = 1
				else:
					sys.exit()
			elif sel == '3':
				os.system('clear')
				s.send(sel.encode())
				tm = s.recv(38)
				print("Time and date is %s" % tm.decode('utf-8'))
				a = input("Enter 1 to back||Enter 0 to exit")
				if a == '1':
					loop = 1
				else:
					sys.exit()
			elif sel == '0':
				print("Exit the system")
				sys.exit()
		else:
			print("exit")
			sys.exit()
			clientsocket.close()
	print("Exit the system")
s.close()


