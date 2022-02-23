import datetime
from blockchain import * 


chain = Chain()
chain.add_transaction(1,2,datetime.datetime.now().timestamp(),Type_tr.GET,0)
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