import datetime
import hashlib
import enum


size_bloc = 50

class Type_tr(enum.Enum):
    GET=1
    SEND=2
    SET=3

def initTypeTR (str):
        if str=="GET":
            return Type_tr.GET
        elif str=="SEND":
            return Type_tr.SEND
        elif str == "SET":
            return Type_tr.SET
        else:
            return 


class Type_node(enum.Enum):
    lumSensor =4
    motionSensor =3
    user=1
    light=2


class Bloc:
    
    def __init__(self, prevHash) :
        print("new bloc create")
        self.prevHash= prevHash
        self.proofOfWork =-1
        self.id_hash ="0"
        self.time=datetime.datetime.now().timestamp()
        self.data =[]
        #self.nextBloc
    
    def isValid(self):

        #detection du seuil de luminosité lorsque la lumiere est allumee 
        t=datetime.datetime.now().timestamp()
        for i in range(0,len(self.data)-1):
            tr=self.data[i]
            switchOff = True
            if tr.dest_id==2 and tr.tr_type==Type_tr.SET and tr.val==1 :
                start=tr.time # debut de l'interval ou la lumiere est allumee
                switchOff=False
            if tr.dest_id==2 and tr.tr_type==Type_tr.SET and tr.val==0:
                last=datetime.datetime.now().timestamp()
                switchOff=True
            if (not switchOff and tr.sender_id==4 and tr.tr_type==Type_tr.SEND and tr.val>=0.7):
                return True
            else :
                return False
        
        return True 

            
            
            

        #detection de passage
        

    def dataToString(self):
        str=""
        for t in self.data:
            str+="/"+t.toString()
        return str

    def mine(self):
        proof= self.proofOfWork
        blocString =str(self.time)+"-"+ self.dataToString()

        id_hash="xx"
        t1=datetime.datetime.now().timestamp()
        while id_hash[0]!= "0"  :
            proof+=1
            string = blocString +"-" +str(proof)
            encoded= string.encode()
            id_hash = hashlib.sha256(encoded).hexdigest()
        #print("id hash :"+id_hash)
        t2=datetime.datetime.now().timestamp()
        print( "mine time ="+str(t2-t1) )
        return (id_hash,proof)

class Transaction:
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
        if len(b.data)>=size_bloc:
            self.closeBlock()
            self.add_transaction(src, dest, time,type_tr, val)
        else:
            b.data.append(Transaction(src, dest, time,type_tr, val))

    def add_tr(self,tr):
        b = self.blocs[self.currentIndex]
        if len(b.data)>=size_bloc:
            self.closeBlock()
            self.add_tr(tr)
        else:
            b.data.append(tr)

    
    def add_bloc(self, prev_hash):
        self.blocs.append(Bloc(prev_hash))
        

    def closeBlock(self):
        currB = self.blocs[self.currentIndex]
        (id_hash,proof )=currB.mine()
        #checkProof
        currB.id_hash=id_hash
        currB.proofOfWork=proof
        #print("Block close:"+ id_hash )
        self.add_bloc(id_hash)
        
        self.currentIndex+=1





