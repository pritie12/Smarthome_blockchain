from itertools import chain
import unittest
from blockchain import * 
import datetime

class TestUtils(unittest.TestCase):




    def test_checkBloc(self):
        chain = Chain()
        
        for i in range(10):
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
        
        for i in range(chain.currentIndex):
            b= chain.blocs[i]
            if i==0:
                self.assertEqual( b.prevHash,"000000" )
                self.assertNotEqual(b.proofOfWork,0)
            elif i== chain.currentIndex-1:
                self.assertEquals( b.prevHash,chain.blocs[i-1].id_hash )
            else:
                self.assertEquals( b.prevHash,chain.blocs[i-1].id_hash )
                self.assertNotEqual(b.proofOfWork,0)
            self.assertNotEqual(b.time,0)



            
            



    def test_req_A0501_1(self):
        c = Chain()
        t=datetime.datetime.now().timestamp()

        #User asking luminosity value
        c.add_transaction(Type_node.user.value,Type_node.lumSensor.value,t,Type_tr.GET,1) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.user.value,t+1,Type_tr.SEND,0.4) 
       
        #User askinging to switch on the light
        c.add_transaction(Type_node.user.value,Type_node.light.value,t+2,Type_tr.SET,1) 
        #Light replying that is on 
        c.add_transaction(Type_node.light.value,Type_node.user.value,t+3,Type_tr.SEND,1)
        #User asking luminosity value
        c.add_transaction(Type_node.user.value,Type_node.lumSensor.value,t+4,Type_tr.GET,1) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.user.value,t+5,Type_tr.SEND,0.8) 
        #self.assertTrue(c.blocs[0].isValid())
        c.add_transaction(Type_node.user.value,Type_node.lumSensor.value,t+6,Type_tr.GET,1) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.user.value,t+7,Type_tr.SEND,0.8) 

         #User askinging to switch on the light
        c.add_transaction(Type_node.user.value,Type_node.light.value,t+8,Type_tr.SET,0) 
        #Light replying that is on 
        c.add_transaction(Type_node.light.value,Type_node.user.value,t+9,Type_tr.SEND,0)

        c.add_transaction(Type_node.user.value,Type_node.lumSensor.value,t+10,Type_tr.GET,1) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.user.value,t+11,Type_tr.SEND,0.4) 

        print(c.blocs[0].isValid())
        self.assertTrue(not c.blocs[0].isValid())

    def test_req_A0501_2(self):
        c = Chain()
        t=datetime.datetime.now().timestamp()

        #User asking luminosity value
        c.add_transaction(Type_node.user.value,Type_node.lumSensor.value,t,Type_tr.GET,1) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.user.value,t+1,Type_tr.SEND,0.4) 
       
        #User askinging to switch on the light
        c.add_transaction(Type_node.user.value,Type_node.light.value,t+2,Type_tr.SET,1) 
        #Light replying that is on 
        c.add_transaction(Type_node.light.value,Type_node.user.value,t+3,Type_tr.SEND,1)
        #User asking luminosity value
        c.add_transaction(Type_node.user.value,Type_node.lumSensor.value,t+4,Type_tr.GET,1) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.user.value,t+5,Type_tr.SEND,0.4) 
        #self.assertTrue(c.blocs[0].isValid())
        c.add_transaction(Type_node.user.value,Type_node.lumSensor.value,t+6,Type_tr.GET,1) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.user.value,t+7,Type_tr.SEND,0.4) 

         #User askinging to switch on the light
        c.add_transaction(Type_node.user.value,Type_node.light.value,t+8,Type_tr.SET,0) 
        #Light replying that is on 
        c.add_transaction(Type_node.light.value,Type_node.user.value,t+9,Type_tr.SEND,0)

        c.add_transaction(Type_node.user.value,Type_node.lumSensor.value,t+10,Type_tr.GET,1) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.user.value,t+11,Type_tr.SEND,0.4) 

        print(c.blocs[0].isValid())
        self.assertFalse(c.blocs[0].isValid())



    def test_req_A0502_2(self):
        c = Chain()
        t=datetime.datetime.now().timestamp()

        c.add_transaction(Type_node.motionSensor.value,Type_node.lumSensor.value,t,Type_tr.GET,0) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.motionSensor,t,Type_tr.SEND,0.6) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.motionSensor,t,Type_tr.GET,0.6) 
        c.add_transaction(Type_node.motionSensor.value,Type_node.lumSensor.value,t,Type_tr.SEND,0) 
        t=t+1
        c.add_transaction(Type_node.motionSensor.value,Type_node.lumSensor.value,t,Type_tr.GET,1) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.motionSensor,t,Type_tr.SEND,0.6) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.motionSensor,t,Type_tr.GET,0.6) 
        c.add_transaction(Type_node.motionSensor.value,Type_node.lumSensor.value,t,Type_tr.SEND,1) 
        t=t+1
        c.add_transaction(Type_node.motionSensor.value,Type_node.lumSensor.value,t,Type_tr.GET,1) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.motionSensor,t,Type_tr.SEND,0.6) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.motionSensor,t,Type_tr.GET,0.6) 
        c.add_transaction(Type_node.motionSensor.value,Type_node.lumSensor.value,t,Type_tr.SEND,1) 
        t=t+1
        c.add_transaction(Type_node.motionSensor.value,Type_node.lumSensor.value,t,Type_tr.GET,1) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.motionSensor,t,Type_tr.SEND,0.6) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.motionSensor,t,Type_tr.GET,0.6) 
        c.add_transaction(Type_node.motionSensor.value,Type_node.lumSensor.value,t,Type_tr.SEND,1) 
        t=t+1
        c.add_transaction(Type_node.motionSensor.value,Type_node.lumSensor.value,t,Type_tr.GET,0) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.motionSensor,t,Type_tr.SEND,0.6) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.motionSensor,t,Type_tr.GET,0.6) 
        c.add_transaction(Type_node.motionSensor.value,Type_node.lumSensor.value,t,Type_tr.SEND,0) 
        t=t+1
        c.add_transaction(Type_node.motionSensor.value,Type_node.lumSensor.value,t,Type_tr.GET,0) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.motionSensor,t,Type_tr.SEND,0.6) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.motionSensor,t,Type_tr.GET,0.6) 
        c.add_transaction(Type_node.motionSensor.value,Type_node.lumSensor.value,t,Type_tr.SEND,0) 

        self.assertFalse(c.blocs[0].isValid())

""" 
    def test_req_A0502_1(self):
        c = Chain()
        t=datetime.datetime.now().timestamp()

        c.add_transaction(Type_node.motionSensor.value,Type_node.lumSensor.value,t,Type_tr.GET,0) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.motionSensor,t,Type_tr.SEND,0.6) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.motionSensor,t,Type_tr.GET,0.6) 
        c.add_transaction(Type_node.motionSensor.value,Type_node.lumSensor.value,t,Type_tr.SEND,0) 
        t=t+1
        c.add_transaction(Type_node.motionSensor.value,Type_node.lumSensor.value,t,Type_tr.GET,1) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.motionSensor,t,Type_tr.SEND,0.6) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.motionSensor,t,Type_tr.GET,0.6) 
        c.add_transaction(Type_node.motionSensor.value,Type_node.lumSensor.value,t,Type_tr.SEND,1) 
        t=t+1
        c.add_transaction(Type_node.motionSensor.value,Type_node.lumSensor.value,t,Type_tr.GET,1) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.motionSensor,t,Type_tr.SEND,0.4) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.motionSensor,t,Type_tr.GET,0.4) 
        c.add_transaction(Type_node.motionSensor.value,Type_node.lumSensor.value,t,Type_tr.SEND,1) 
        t=t+1
        c.add_transaction(Type_node.motionSensor.value,Type_node.lumSensor.value,t,Type_tr.GET,1) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.motionSensor,t,Type_tr.SEND,0.4) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.motionSensor,t,Type_tr.GET,0.4) 
        c.add_transaction(Type_node.motionSensor.value,Type_node.lumSensor.value,t,Type_tr.SEND,1) 
        t=t+1
        c.add_transaction(Type_node.motionSensor.value,Type_node.lumSensor.value,t,Type_tr.GET,0) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.motionSensor,t,Type_tr.SEND,0.4) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.motionSensor,t,Type_tr.GET,0.4) 
        c.add_transaction(Type_node.motionSensor.value,Type_node.lumSensor.value,t,Type_tr.SEND,0) 
        t=t+1
        c.add_transaction(Type_node.motionSensor.value,Type_node.lumSensor.value,t,Type_tr.GET,0) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.motionSensor,t,Type_tr.SEND,0.6) 
        c.add_transaction(Type_node.lumSensor.value,Type_node.motionSensor,t,Type_tr.GET,0.6) 
        c.add_transaction(Type_node.motionSensor.value,Type_node.lumSensor.value,t,Type_tr.SEND,0) 

        self.assertTrue(c.blocs[0].isValid())"""
        


if __name__ == '__main__':
    unittest.main()