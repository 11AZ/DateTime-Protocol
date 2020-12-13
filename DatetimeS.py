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

client_socket.send(bytes("Welcome to the server", "utf-8"))

#close client socket
client_socket.close()

#Close server socket
s.close()
