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
            Input=input("Entrez l'id de l'objet")
            dest= int(Input)
            Input=input("Entrez la valeur")
            val = int(Input)
            self.sendTransaction(Transaction(self.id,dest,datetime.datetime.now().timestamp()),Type_tr.SET,val)
        elif (Input=="2"):
            Input=input("Entrez l'id de l'objet")
            dest= int(Input)
            self.sendTransaction(Transaction(self.id,dest,datetime.datetime.now().timestamp()),Type_tr.GET,self.val)
        
        else:
            print("retry later")




try :
    port = sys.argv[1]
    host=sys.argv[2]
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
    res = client.receiveMsg()
    




