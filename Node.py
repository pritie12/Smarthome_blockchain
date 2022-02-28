from blockchain import Chain, Transaction , initTypeTR
import socket

host = '127.0.0.1'
port = 2004

socketSize = 1024
class Node:
    def __init__(self,type,param) :
        self.id=-1
        self.type_n = type
        self.param = param
        self.val =0.0
        self.bloc=Chain()
        self.nodes=[]
        
    
    def connecServer(self,host, port):
        self.client = socket.socket()
        try:
            self.client.connect((host, port))
            self.receiveMsg() # to init the id
            self.client.send(str.encode("cl:"+str(self.id)+","+self.type_n))
        except socket.error as e:
            print(str(e))

    def sendTransaction(self,tr):
        msg ="tr:"+tr.toString()  # transaction
        print (msg)
        self.client.send(str.encode(msg))
    
    def sendBlockValidation(self, res): 
        msg="bv:"+ str(res)
        self.client.send(str.encode(msg))
    
    def sendProofOfWork(self, pow):
        msg="po:"+ str(pow)
        self.client.send(str.encode(msg))
    
    def sendProofValidation(self,res):
        msg="pv:"+ str(pow)
        self.client.send(str.encode(msg))


    
    def receiveMsg(self):
        msg =(self.client.recv(socketSize)).decode('utf-8')
        print(msg)
        msgSplited = msg.split(":")
        typeMsg = msgSplited[0]
        if typeMsg=="tr":
            trSting =msgSplited[1].split(",")
            tr =Transaction (trSting[0],trSting[1],trSting[2],initTypeTR(trSting[3]),trSting[4])
            return (typeMsg,tr)
        elif typeMsg=="id":
            self.id=int(msgSplited[1])
        elif typeMsg=="cl":
            self.nodes.append((int(msgSplited[1]),msgSplited[2])) # pb doublons
        else:
            return (msgSplited[0], msgSplited[1])

        



    

