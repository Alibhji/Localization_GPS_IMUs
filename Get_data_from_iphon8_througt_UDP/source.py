import os
os.system('conda activate qt36')
os.system('pyuic5 ./mainui.ui > mainui.py')
# from pyqtgraph.widgets.PlotWidget import PlotWidget

from mainui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QDialog,QWidget,QMainWindow,QLabel
import sys
from PyQt5.QtCore import Qt ,QTimer
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem
import socket
import subprocess
import pyqtgraph
import numpy as np
import matplotlib.pyplot as plt



class Appwindow(QMainWindow):
    def __init__(self):
        super(Appwindow,self).__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.timer=QTimer()
        # self.timer.timeout.connect(self.tick)
        self.timer.timeout.connect(self.UDP_Srver)
        self.ui.btn_start_udp_server.clicked.connect(self.buttonClicked)
        self.ui.btn_stop_udp_server.clicked.connect(self.btn_stop)
        # self.timer.stop()
        pyqtgraph.setConfigOption('background', 'w') #before loading widget
       
        
        self.t=np.array([0])
        self.x=np.array([0])
        self.pocket_num=0
        
        
    def tick(self):
        print ('tick')

    def buttonClicked(self):
        
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        rate=(1/float(self.ui.in_Rate.text())*1000)
        
        self.timer.start(rate) 
        print((rate),' ms delay.')


    def btn_stop(self):
        self.timer.stop()
        plt.plot(self.t,self.x)
        plt.show()
        print(self.t,self.x)
            

    def UDP_Srver(self):
        # IP="0.0.0.0"
        IP=self.ui.in_IP.text()
        # PORT=50890
        PORT=int(self.ui.in_Port.text())
        

        with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as soc:
            soc.bind((IP, PORT))
            data=soc.recv(1024)
            
            data=str(data).split(',')
            if data:
                self.x=np.append(self.x,data[21])
                self.t=np.append(self.t,(self.pocket_num))
                self.pocket_num+=1
            # self.ui.graphicsView
            # pyqtgraph.plot(self.t,self.x)
                self.ui.treeWidget.setHeaderLabels(["A", "B"])
                Item_label=['Time','DataGram#','','Device','','Latitude','Longtitude','Altitude','speed','course','Vertical acc' ,'Horizontal acc','?1','?2','MicroTesl-X','MicroTesl-Y' ,'MicroTesl-Z','True north','Magnet north','Accuracy', '??','Pitch','Roll','Yaw','??', 'Rote-rate-X' ,'Rote-rate-Y','Rote-rate-Z' ]
                self.ui.treeWidget.clear()
                for cnt ,i in enumerate(data):
                    Item1=QTreeWidgetItem()
                    Item2=QTreeWidgetItem()
                    Item1.setText(1, str(i))
                    Item1.setText(0, str(cnt))
                    if(len(Item_label) > cnt):
                        Item1.setText(0, str(cnt)+'- '+Item_label[int(cnt)])
                    self.ui.treeWidget.addTopLevelItem(Item1)

            

if __name__ == "__main__":
    app=QApplication(sys.argv)
    w=Appwindow()
    w.show()   
    
    sys.exit(app.exec())
    


            
            