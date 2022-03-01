import socket
import os
from _thread import *
ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
Nb_client = 0
current_tr=""
clients =[]

try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(5)

def multi_threaded_client(connection):
    connection.sendall(str.encode("id:"+str(Nb_client)))
    data_n = connection.recv(2048)

    while True:
        data = connection.recv(2048)
        current_tr=data
        response = current_tr.decode('utf-8')
        if not data:
            break
        
        for c in clients:
                c.sendall(str.encode(response))
        #connection.sendall(str.encode(response))
    connection.close()

i=0

while True:
    Client, address = ServerSideSocket.accept()
    clients.append(Client)
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    Nb_client += 1
    print('Thread Number: ' + str(Nb_client))
ServerSideSocket.close()