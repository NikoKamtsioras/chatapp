from settings import *
import socket

s = socket.socket()

port = default_port

s.connect((server_ip, port))

while True:
    data = s.recv(1024).decode()
    if data:
        print(data)
    
s.close()