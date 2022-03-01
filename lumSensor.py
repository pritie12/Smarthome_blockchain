import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
                             QMenu, QPushButton, QRadioButton, QVBoxLayout, QWidget, QSlider, QLabel)
from PyQt5.QtGui import QFont

import sys
from Node import *
from blockchain import Transaction, Type_tr,Type_node
import datetime


class slider(QWidget):
   def __init__(self, parent = None):
      super(slider, self).__init__(parent)

      layout = QVBoxLayout()
      self.l1 = QLabel("Luminosity:")
      self.l1.setAlignment(Qt.AlignCenter)
      layout.addWidget(self.l1)
		
      self.sl = QSlider(Qt.Horizontal)
      self.sl.setMinimum(1)
      self.sl.setMaximum(100)
      self.sl.setValue(50)
      self.sl.setTickPosition(QSlider.TicksBelow)
      self.sl.setTickInterval(10)
		
      layout.addWidget(self.sl)
      self.sl.valueChanged.connect(self.valuechange)
      self.setLayout(layout)
      self.setWindowTitle("Lumosity sensor")

   def valuechange(self):
      value = self.sl.value()
      self.l1.setText("Luminosity: "+str(value)+" %")





class lumSensorN(Node):
    def __init__(self):
        super().__init__("sensor",0.5)
        self.app = QApplication(sys.argv)
        self.slider = slider()
        self.slider.show()

    def checkUserparam():
        return True
    


    def mainCommands(self):
        self.val= self.get_sensor_val()
        if self.val< self.param and self.checkUserparam():
            self.sendTransaction(Transaction(self.id,Type_node.light.value,datetime.datetime.now().timestamp(),Type_tr.SET,1))
        else:
            print("retry later")
    
    def trResponse(self,type,tr):
        if tr.dest_id==self.id:
            if tr.tr_type ==Type_tr.SET : #condition
                self.param=tr.val
                self.sendTransaction(Transaction(self.id,tr.sender,datetime.datetime.now().timestamp(),Type_tr.SEND,self.param))
                # envoie un send val
            if tr.tr_type ==Type_tr.GET:
                #envoie un send val
                self.sendTransaction(Transaction(self.id,tr.sender,datetime.datetime.now().timestamp(),Type_tr.SEND,self.val))

            
            if tr.tr_type ==Type_tr.SEND:
                print("node "+ tr.sender+": "+ tr.val)
    
    def get_sensor_val(self):
        return self.slider.sl.value()
                





try :
    host=sys.argv[1]
    port = int(sys.argv[2])
    
    print(port, host)
except :
    print ("default port and host")
    host = '127.0.0.1'
    port = 2004



client=lumSensorN()

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
    sys.exit(client.app.exec_())


