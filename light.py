#light.py
import sys
from Node import *
from blockchain import Transaction, Type_tr
import datetime


class MotorN(Node):
    def __init__(self,param):
        return super().__init__("motor",param) # param in sec

    def mainCommands(self):
        print("Commandes possibles : ")
        print("1-Set param")
        print("2-Get value")
        Input=input("Que voulez-vous faire?")
        if(Input=="1"):
            Input=input("Entrez l'id de l'objet")
            dest= int(Input)
            Input=input("Entrez la valeur")
            val = int(Input)
            self.sendTransaction(Transaction(self.id,dest,datetime.datetime.now().timestamp(),Type_tr.SET,val))
        elif (Input=="2"):
            Input=input("Entrez l'id de l'objet")
            dest= int(Input)
            self.sendTransaction(Transaction(self.id,dest,datetime.datetime.now().timestamp()),Type_tr.GET,self.val)
        
        else:
            print("retry later")
    
    def trResponse(self,type,tr):
        if tr.dest==self.id:
            '''if tr._type ==Type_tr.SET:
                self.val=tr.val
                # envoie un send val'''
            if tr._type ==Type_tr.GET:
                #envoie un send vql
                self.sendTransaction(Transaction(self.id,tr.sender,datetime.datetime.now().timestamp(),Type_tr.SEND,self.val))

            
            if tr._type ==Type_tr.SEND:
                print("node "+ tr.sender+": "+ tr.val)
                #type SEND ???





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

while True:
    #client.mainCommands()
    (typeMsg,arg) = client.receiveMsg()
    if typeMsg=="tr":
        client.bloc.add_tr(arg)
        client.trResponse(typeMsg,arg)






