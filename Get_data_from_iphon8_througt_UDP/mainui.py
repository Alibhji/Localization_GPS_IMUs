# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './mainui.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1012, 890)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_start_udp_server = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start_udp_server.setGeometry(QtCore.QRect(20, 10, 151, 28))
        self.btn_start_udp_server.setObjectName("btn_start_udp_server")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(440, 10, 531, 821))
        self.treeWidget.setLineWidth(1)
        self.treeWidget.setObjectName("treeWidget")
        self.btn_stop_udp_server = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop_udp_server.setGeometry(QtCore.QRect(20, 40, 151, 28))
        self.btn_stop_udp_server.setObjectName("btn_stop_udp_server")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 150, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 31, 16))
        self.label_2.setObjectName("label_2")
        self.in_IP = QtWidgets.QLineEdit(self.centralwidget)
        self.in_IP.setGeometry(QtCore.QRect(50, 180, 101, 22))
        self.in_IP.setObjectName("in_IP")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 210, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 180, 31, 16))
        self.label_4.setObjectName("label_4")
        self.in_Rate = QtWidgets.QLineEdit(self.centralwidget)
        self.in_Rate.setGeometry(QtCore.QRect(50, 150, 31, 22))
        self.in_Rate.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.in_Rate.setObjectName("in_Rate")
        self.in_Port = QtWidgets.QLineEdit(self.centralwidget)
        self.in_Port.setGeometry(QtCore.QRect(50, 210, 91, 22))
        self.in_Port.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.in_Port.setObjectName("in_Port")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1012, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_start_udp_server.setText(_translate("MainWindow", "Start UDP Server"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Press \"Start UDP bottom to start getting data\""))
        self.btn_stop_udp_server.setText(_translate("MainWindow", "Stop"))
        self.label.setText(_translate("MainWindow", "HZ"))
        self.label_2.setText(_translate("MainWindow", "Rate"))
        self.in_IP.setText(_translate("MainWindow", "0.0.0.0"))
        self.label_3.setText(_translate("MainWindow", "PORT"))
        self.label_4.setText(_translate("MainWindow", "IP"))
        self.in_Rate.setText(_translate("MainWindow", "20"))
        self.in_Port.setText(_translate("MainWindow", "50890"))
