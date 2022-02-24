import datetime
import hashlib
from logging.config import valid_ident
import enum




class Type_tr(enum.Enum):
    GET=1
    SEND=2
    SET=3


class Bloc:
    
    def __init__(self, prevHash) :
        print("new bloc create")
        self.prevHash= prevHash
        self.proofOfWork =0
        self.id_hash ="0"
        self.time=datetime.datetime.now().timestamp()
        self.data =[]
        #self.nextBloc
    
    def idValid(self):
        return True

    def dataToString(self):
        str=""
        for t in self.data:
            str+="/"+t.toString()
        return str

    def mine(self):
        proof= self.proofOfWork
        blocString =str(self.time)+"-"+ self.dataToString()

        string = blocString +"-" +str(proof)
        encoded= string.encode()
        id_hash = hashlib.sha256(encoded).hexdigest()

        return (id_hash,proof)

class Trasaction:
    def __init__(self,src, dest, time,type_tr, val):
        self.sender_id=src
        self.dest_id=dest
        self.time=time
        self.tr_type=type_tr
        self.val=val
    
    def toString(self):
        res=str(self.sender_id)+","+str(self.dest_id)+","+str(self.time)+","+self.tr_type.name+","+str(self.val)
        #res="hello"
        return res

class Chain:
    def __init__(self) :
        self.blocs=[]
        self.blocs.append(Bloc("000000"))
        self.currentIndex =0
        self.num_node=0
    
    def add_transaction(self,src, dest, time,type_tr, val):
        b = self.blocs[self.currentIndex]
        if len(b.data)>=10:
            self.closeBlock()
            self.add_transaction(src, dest, time,type_tr, val)
        else:
            b.data.append(Trasaction(src, dest, time,type_tr, val))
    
    def add_bloc(self, prev_hash):
        self.blocs.append(Bloc(prev_hash))
        

    def closeBlock(self):
        currB = self.blocs[self.currentIndex]
        (id_hash,proof )=currB.mine()
        #checkProof
        currB.id_hash=id_hash
        currB.proofOfWork=proof
        print("Block close:"+ id_hash )
        self.add_bloc(id_hash)
        
        self.currentIndex+=1





