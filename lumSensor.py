import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
                             QMenu, QPushButton, QRadioButton, QVBoxLayout, QWidget, QSlider, QLabel)
from PyQt5.QtGui import QFont

import sys
from Node import *
from blockchain import Transaction, Type_tr
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





class UserN(Node):
    def __init__(self):
        super().__init__("sensor",0.5)
        self.app = QApplication(sys.argv)
        self.slider = slider()
        self.slider.show()

    


    def mainCommands(self):
        self.val= self.get_sensor_val()
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
    port = sys.argv[2]
    
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
    (typeMsg,arg) = client.receiveMsg()
    if typeMsg=="tr":
        client.bloc.add_tr(arg)
        client.trResponse(typeMsg,arg)
    sys.exit(client.app.exec_())


