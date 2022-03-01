#light.py
from pydoc import cli
import sys
from Node import *
from blockchain import Transaction, Type_tr
import datetime


class MotorN(Node):
    def __init__(self,param):
        return super().__init__("motor",param) # param in sec

    def mainCommands(self):
        print("Commandes possibles : ")
        print("1-voirval")

        Input=input("Que voulez-vous faire?")
        if(Input=="1"):
            print(str(self.val))

        else:
            print("retry later")
    
    def trReponse(self,type,tr):
        print("rep"+str(tr.toSting())+" "+str(self.id)+" ")
        if tr.dest_id==self.id:
            if tr.tr_type ==Type_tr.SET :
                self.val=tr.val
                if(tr.val ==1):
                    print("switch on")
                else:
                     print("switch off")
                tr = Transaction(self.id,tr.sender,datetime.datetime.now().timestamp(),Type_tr.SEND,self.val)
                self.sendTransaction(tr)
                # envoie un send val
            if tr._type ==Type_tr.GET:
                #envoie un send val
                tr = Transaction(self.id,tr.sender,datetime.datetime.now().timestamp(),Type_tr.SEND,self.val)
                self.sendTransaction(tr)







try :
    host=sys.argv[1]
    port = sys.argv[2]
    
    print(port, host)
except :
    print ("default port and host")
    host = '127.0.0.1'
    port = 2004



client=MotorN(60*5)

chain = client.bloc

client.connecServer(host,port)
print("id"+str(client.id))
while True:
    try:
    #client.mainCommands()
        (typeMsg,arg) = client.receiveMsg()
        print("MA"+typeMsg)
        if typeMsg=="tr":
            client.bloc.add_tr(arg)
            client.trReponse(typeMsg,arg)
        client.mainCommands()
        
    except :
            i=0






