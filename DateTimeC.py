import socket
import sys
import datetime
#Create client socket
s = socket.socket()

#Server ip address and port use
host = "192.168.0.101"
port = 8888

#Connect to server
print(f"[+] Connecting to {host}:{port}")
s.connect((host,port))
print("[+] connected")

#User input
user = input("Enter <today> to know today date and time:")
s.send(f"{user}".encode())

#Close socket
s.close()
