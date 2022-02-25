from blockchain import Chain, Transaction , initTypeTR
import socket



socketSize = 1024
class Node:
    def __init__(self,type,param) :
        self.id
        self.type_n = type
        self.param = param
        self.val =0.0
        self.bloc=Chain()
    
    def connecServer(self,host, port):
        self.client = socket.socket()
        try:
            self.client.connect((host, port))
        except socket.error as e:
            print(str(e))

    def sendTransaction(self,tr):
        msg ="tr:"+tr.toString()
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
        msg =self.client.recv(socketSize)
        msgSplited = msg.split(":")
        typeMsg = msgSplited[0]
        if typeMsg=="tr":
            trSting =msgSplited[1].split(",")
            tr =Transaction (trSting[0],trSting[1],trSting[2],initTypeTR(trSting[3]),trSting[4])
            return (typeMsg,tr)
        else:
            return (msgSplited[0], msgSplited[1])

        


class UserN(Node):
    def __init__(self,param):
        return super().__init__("user",param)
    

