#!/usr/bin/env python 

import socket

host = ''
port = 50000
backlog = 1 
size = 3 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog) 
while 1: 
    client, address = s.accept() 
    data = client.recv(size) 
    if data: 
        client.send(data) 
    client.close()
