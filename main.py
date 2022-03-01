import datetime
from blockchain import * 
from Node import*

host = '127.0.0.1'
port = 2004
"""
client=Node("user",0)

chain = client.bloc

#client.connecServer(host,port)

tr= Transaction(1,2,datetime.datetime.now().timestamp(),Type_tr.GET,0)
client.sendTransaction(tr)
res=client.receiveMsg()
chain.add_transaction(1,2,datetime.datetime.now().timestamp(),Type_tr.GET,0)
while True:
    res = client.client.recv(1024)
    print(res.decode('utf-8'))"""

chain= Chain()
for i in range (100):
    chain.add_transaction(2,1,datetime.datetime.now().timestamp(),Type_tr.SEND,0.8)
    chain.add_transaction(1,2,datetime.datetime.now().timestamp(),Type_tr.GET,0)
    chain.add_transaction(2,1,datetime.datetime.now().timestamp(),Type_tr.SEND,0.9)
    chain.add_transaction(1,2,datetime.datetime.now().timestamp(),Type_tr.GET,0)
    chain.add_transaction(2,1,datetime.datetime.now().timestamp(),Type_tr.SEND,1.0)
    chain.add_transaction(1,2,datetime.datetime.now().timestamp(),Type_tr.GET,0)
    chain.add_transaction(2,1,datetime.datetime.now().timestamp(),Type_tr.SEND,1.0)
    chain.add_transaction(1,2,datetime.datetime.now().timestamp(),Type_tr.GET,0)
    chain.add_transaction(2,1,datetime.datetime.now().timestamp(),Type_tr.SEND,0.9)
    chain.add_transaction(1,2,datetime.datetime.now().timestamp(),Type_tr.GET,0)
    chain.add_transaction(2,1,datetime.datetime.now().timestamp(),Type_tr.SEND,0.8)

print("bloc 0")
print(chain.blocs[0].dataToString())
print("bloc 1")
print(chain.blocs[1].dataToString())