import unittest
from blockchain import * 
import datetime

class TestUtils(unittest.TestCase):
    def test_checkBloc(self):
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






if __name__ == '__main__':
    unittest.main()