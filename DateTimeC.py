import time
import socket
import sys
from tqdm import tqdm , trange
# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
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

#receive answer from server
msg=s.recv(1024)
print(msg.decode("utf-8"))

# Receive no more than 1024 bytes
tm = s.recv(1024)
print("The time got from the server is %s" % tm.decode('utf-8'))

s.close()
