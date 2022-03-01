import sys
from Node import *
from blockchain import Transaction, Type_tr
import datetime


class UserN(Node):
    def __init__(self,param):
        return super().__init__("user",param)

    def mainCommands(self):
        print("Commandes possibles : ")
        print("1-Set param")
        print("2-Get value")
        Input=input("Que voulez-vous faire?")
        if(Input=="1"):
            Input=input("Entrez l'id de l'objet: ")
            dest= int(Input)
            Input=input("Entrez la valeur: ")
            val = int(Input)
            tr=Transaction(self.id,dest,datetime.datetime.now().timestamp(),Type_tr.SET,val)
            self.sendTransaction(tr)
           # self.bloc.add_tr(tr)
        elif (Input=="2"):
            Input=input("Entrez l'id de l'objet: ")
            dest= int(Input)
            tr=Transaction(self.id,dest,datetime.datetime.now().timestamp(),Type_tr.GET,self.val)
            self.sendTransaction(tr)
            #self.bloc.add_tr(tr)
        elif (Input=="3"):
            print(self.bloc.blocs[0].dataToString())
        
        else:
            print("retry later")
    
    def trResponse(self,type,tr):
        if tr.dest_id==self.id:
            if tr.tr_type ==Type_tr.SET and tr.sender_id== self.id: #condition
                self.val=tr.val
                self.sendTransaction(Transaction(self.id,tr.sender,datetime.datetime.now().timestamp(),Type_tr.SEND,self.val))
                # envoie un send val
            if tr.tr_type ==Type_tr.GET:
                #envoie un send val
                self.sendTransaction(Transaction(self.id,tr.sender,datetime.datetime.now().timestamp(),Type_tr.SEND,self.val))

            
            if tr.tr_type ==Type_tr.SEND:
                print("node "+ tr.sender+": "+ tr.val)
                





try :
    host=sys.argv[1]
    port = int(sys.argv[2])
    
    print(port, host)
except :
    print ("default port and host")
    host = '127.0.0.1'
    port = 2004



client=UserN(0)

chain = client.bloc

client.connecServer(host,port)

while True:
    client.mainCommands()
    try:
        (typeMsg,arg) = client.receiveMsg()
        if typeMsg=="tr":
            client.bloc.add_tr(arg)
            client.trResponse(typeMsg,arg)
    except:
        i=0







