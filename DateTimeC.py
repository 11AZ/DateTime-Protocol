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

#Front page function
def fmenu():
	print("-------------------------------WELCOME TO DATETIME PROGRAM-------------------------")
	print("|1| Go to date time program")
	print("|0| Exit the program")
	while True:
		opt = input("Enter your choice:")
		if opt == '1':
			Datetime()
		elif opt == '0':
			break
		else:
			print("invalid choice")
			fmenu()
	sys.exit()

#Date tiem menu
def Datetime():
	print("This is a simple date time server")
	print("[1] To check for today date and time")
	print("[2] To check for yesterday date")
	print("[3] To check for tommorrow date")
	print("[99] to go back to the Main menu")
	print("[0] to exit the program")
	while True:
		sel = input("Enter your choice")
		if sel == '1':
			s.send(sel.encode())
			msg = s.recv(36)
			print("Today time :%s" % msg.decode('utf-8'))
		elif sel == '2':
			s.send(sel.encode())
			msg = s.recv(23)
			print("Yesterday date is %s" % msg.decode("utf-8"))
		elif sel == '3':
			s.send(sel.encode())
			msg = s.recv(23)
			print("Tommorrow date is %s" % msg.decode("utf-8"))
		elif sel == '99':
			fmenu()
		elif sel == '0':
			sys.exit()
		else:
			print("No input from server")



#Main
fmenu()

