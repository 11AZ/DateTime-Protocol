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

#receive answer from server
msg = s.recv(1024)
print(msg.decode("utf-8"))

#Close socket
s.close()
