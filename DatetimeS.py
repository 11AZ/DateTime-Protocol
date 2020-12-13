import socket
import datetime
import sys
#Create server socket

s=socket.socket()
print(f"[+] socket successfully created")

#Server host
host = "192.168.0.101"
#port
port = 8888

#bind the socket
s.bind((host,port))
print(f"[+] socket binded to" + str(port))

#Enable socket to accept connection
s.listen(5)
print(f"[+] Socket is listening")

#Accept connection
client_socket, address =s.accept()

#Show the sender is connected
print(f"[+] {address} is connected")
#Reply to client date and time
data = client_socket.recv(1024).decode()
print(data)
client_socket.send("Current date and time :"+str(datetime.datetime.now()))
#close client socket
client_socket.close()

#Close server socket
s.close()
