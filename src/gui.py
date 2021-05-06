# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import *
from PyQt5 import QtCore, QtGui, QtWidgets
import os,sys,subprocess
import gui_main,gui_stalling,gui_forwarding
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QGroupBox, QVBoxLayout, QHBoxLayout, QCheckBox, QRadioButton
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRect

class Ui_MainWindow(object):
    pc=0
    ir=0
    reg=0
    idi=0
    dd=0
    clock=0
    pc_f=0
    pc_t=0
    outtext=0
    pipeline=0
    varlist=[]
    bdd=[]
    cpc=[]
    cachesize=0
    blocksize=0
    sa_ways=0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1360, 821)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(550, 0, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 70, 131, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(445, 230, 131, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 750, 89, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(290, 380, 650, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(280, 20, 20, 791))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(930, 20, 20, 791))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(940, 200, 420, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(940, 280, 420, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(310, 430, 256, 331))
        self.tableWidget.setRowCount(32)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(580, 390, 20, 441))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 390, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(700, 390, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 50, 71, 17))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 80, 271, 661))
        self.textBrowser.setObjectName("textBrowser")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(620, 420, 291, 341))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(13)
        
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_7.setGeometry(QtCore.QRect(1200, 215, 150, 70))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(305, 230, 131, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(385, 120, 101, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(320, 280, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(320, 330, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(370, 280, 181, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(370, 320, 181, 31))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(720, 40, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1050, 40, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(950, 230, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1050, 290, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_10")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(320, 165, 81, 31))
        self.checkBox = QPushButton(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(980, 80, 82, 17))
        self.checkBox.setFont(QtGui.QFont("sanserif", 11))
        self.radioBox_2 = QRadioButton(self.centralwidget)
        self.radioBox_2.setObjectName(u"radioBox_2")
        self.radioBox_2.setGeometry(QRect(1180, 120, 82, 17))
        self.radioBox_2.setFont(QtGui.QFont("sanserif", 11))
        self.radioBox_3 = QRadioButton(self.centralwidget)
        self.radioBox_3.setObjectName(u"radioBox_3")
        self.radioBox_3.setGeometry(QRect(980, 120, 82, 17))
        self.radioBox_3.setFont(QtGui.QFont("sanserif", 11))
        self.checkBox_4 = QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(1180, 80, 82, 17))
        self.checkBox_4.setFont(QtGui.QFont("sanserif", 11))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(1000, 180, 91, 21))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit")
        self.lineEdit_2.setGeometry(QRect(1000, 200, 91, 21))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit")
        self.lineEdit_3.setGeometry(QRect(1000, 220, 91, 21))
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit")
        self.lineEdit_4.setGeometry(QRect(1000, 240, 91, 21))
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(1150, 180, 91, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_6.setGeometry(QtCore.QRect(390, 165, 101, 31))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_3.setGeometry(QtCore.QRect(620, 80, 281, 301))
        self.tableWidget_3.setRowCount(10)
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(620, 70, 281, 31))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(580, 60, 20, 381))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 932, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.radioBox_2.setHidden(True)
        self.radioBox_3.setHidden(True)
        self.checkBox.setStyleSheet("background-color : red")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tableWidget.setColumnWidth(0,50)
        self.tableWidget.setColumnWidth(1,42)
        self.tableWidget.setColumnWidth(2,42)
        self.tableWidget.setColumnWidth(3,42)
        self.tableWidget.setColumnWidth(4,42)
        self.tableWidget_2.setColumnWidth(0,80)
        self.tableWidget_2.setColumnWidth(1,42)
        self.tableWidget_2.setColumnWidth(2,42)
        self.tableWidget_2.setColumnWidth(3,42)
        self.tableWidget_2.setColumnWidth(4,42)
        self.tableWidget_3.setColumnWidth(1,135)
        self.tableWidget_4 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_4.setGeometry(QtCore.QRect(960, 330, 381, 471))
        self.tableWidget_4.setRowCount(2000)
        self.tableWidget_4.setColumnCount(2000)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnWidth(0,80)
        for i in range(self.tableWidget_4.columnCount()):
            self.tableWidget_4.setColumnWidth(i+1,45)

    def loaddata(self,dic):
        i=0
        for x in dic:
            temp2="x"+str(x)
            self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(temp2))
            temp1=dic[x].upper()
            if(temp1[0]=='-'):
                temp1=hex(int(temp1,16)+(1<<32))
            for j in range(1,6):
                self.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(temp1[2*j:2*(j+1)]))
            i+=1


    def loaddata2(self,dic):
        i=0
        self.tableWidget_3.setRowCount(max(11,len(dic)))
        for x in dic:
            self.tableWidget_3.setItem(i,0,QtWidgets.QTableWidgetItem(x))
            temp1=dic[x].upper()
            self.tableWidget_3.setItem(i,1,QtWidgets.QTableWidgetItem(temp1))
            i+=1
        
    
    def loaddata3(self,dic):
        
        t1=list(dic.keys())
        newdic={}
        for i in range(len(t1)):
            newdic[int(t1[i],16)]=dic[t1[i]][2:]
            t1[i]=int(t1[i],16)
        t1.sort()
        fina={}
        nice=0
        for i in range(len(t1)):
            if(t1[i]%4==0):
                nice=t1[i]//4
                fina[hex(nice*4)]=newdic[t1[i]]+"000000"
            else:
                nice=t1[i]//4
                etc=t1[i]%4
                if(fina.get(hex(nice*4),-1)==-1):
                    fina[hex(nice*4)]="00"*(etc)+newdic[t1[i]]+"00"*(3-etc)
                else:
                    fina[hex(nice*4)]=fina[hex(nice*4)][:2*(etc)]+newdic[t1[i]]+fina[hex(nice*4)][2*(etc+1):]
        self.tableWidget_2.setRowCount(max(13,len(fina)))
        i=0
        for x in fina:
            self.tableWidget_2.setItem(i,0,QtWidgets.QTableWidgetItem(x))
            temp1=fina[x].upper()
            for j in range(1,6):
                self.tableWidget_2.setItem(i,j,QtWidgets.QTableWidgetItem(temp1[2*(j-1):2*(j)]))
            i+=1
    def loaddata4(self,lis,dicti):
        self.clock+=1
        self.tableWidget_4.scrollToItem(self.tableWidget_4.item(len(lis), self.clock))
        dic=[]
        for x in range(len(dicti)):
            dic.append(dicti[x])
        
        if(len(dic[4])==0):
            dic[4].append(-1)
        if(len(dic[3])==0):
            dic[3].append(-1)
        if(len(dic[2])==0):
            dic[2].append(-1)
        if(len(dic[1])==0):
            dic[1].append(-1)
        if(len(dic[0])==0):
            dic[0].append(-1)      
        for i in range(len(lis)):
            if(lis[i]==-1):
                continue
            else:
                if(dic[4][0]==lis[i]):
                    lis[i]=-1
                    x='W'
                    dic[4][0]=-1
                    self.tableWidget_4.setItem(i,self.clock,QtWidgets.QTableWidgetItem(x))
                    y=str(self.tableWidget_4.item(i,self.clock-1))
                    if(y==x):
                        self.tableWidget_4.item(i,self.clock).setBackground(QtGui.QColor(0,100,100))
                        break
                elif(dic[3][0]==lis[i]):
                    x='M'
                    self.tableWidget_4.setItem(i,self.clock,QtWidgets.QTableWidgetItem(x))
                    dic[3][0]=-1
                    y=str(self.tableWidget_4.item(i,self.clock-1))
                    if(y==x):
                        self.tableWidget_4.item(i,self.clock).setBackground(QtGui.QColor(0,100,100))
                        break
                elif(dic[2][0]==lis[i]):
                    x='E'
                    y=str(self.tableWidget_4.item(i,self.clock-1))
                    if(y==x):
                        self.tableWidget_4.item(i,self.clock).setBackground(QtGui.QColor(0,100,100))
                        break
                    self.tableWidget_4.setItem(i,self.clock,QtWidgets.QTableWidgetItem(x))
                    dic[2][0]=-1
                elif(dic[1][0]==lis[i]):
                    x='D'
                    
                    if(i==0):
                        self.tableWidget_4.setItem(i,self.clock,QtWidgets.QTableWidgetItem(x))
                        dic[1][0]=-1
                        self.tableWidget_4.setItem(i,self.clock-1,QtWidgets.QTableWidgetItem("F"))
                    else:
                        self.tableWidget_4.setItem(i,self.clock,QtWidgets.QTableWidgetItem(x))
                        dic[1][0]=-1
                        y=self.tableWidget_4.item(i,self.clock-1)
                        if(y!=None):
                            y=y.text()
                        
                        if(y==x):
                            self.tableWidget_4.item(i,self.clock).setBackground(QtGui.QColor(0,100,100))
                            break
                elif(dic[0][0]==lis[i]):
                    x='F'
                    self.tableWidget_4.setItem(i,self.clock,QtWidgets.QTableWidgetItem(x))
                    dic[0][0]=-1
                    y=str(self.tableWidget_4.item(i,self.clock-1))
                    if(y==x):
                        self.tableWidget_4.item(i,self.clock).setBackground(QtGui.QColor(0,100,100))
                        break
        self.clock-=1

                

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "RISC-V Simulator"))
        self.pushButton.setText(_translate("MainWindow", "README"))
        self.pushButton_2.setText(_translate("MainWindow", "Open data.mc"))
        self.pushButton_3.setText(_translate("MainWindow", "RUN"))
        self.pushButton_4.setText(_translate("MainWindow", "Output Log"))
        self.pushButton_7.setText(_translate("MainWindow", "Print Pipeline Registers"))
        self.label_3.setText(_translate("MainWindow", "Register View"))
        self.label_4.setText(_translate("MainWindow", "Memory View"))
        self.label_2.setText(_translate("MainWindow", "Output"))
        
        self.pushButton_5.setText(_translate("MainWindow", "STEP"))
        self.pushButton_6.setText(_translate("MainWindow", "ASSEMBLE"))
        self.label_5.setText(_translate("MainWindow", "PC :"))
        self.label_6.setText(_translate("MainWindow", "IR:"))
        self.checkBox.setText(_translate("MainWindow", u"Pipelined Execution", None))
        self.radioBox_2.setText(_translate("MainWindow", u"Stalling", None))
        self.radioBox_3.setText(_translate("MainWindow", u"Data Forwarding", None))
        self.checkBox_4.setText(_translate("MainWindow", u"Print Pipeline Registers", None))
        
        self.label_7.setText(_translate("MainWindow", "Instructions"))
        self.label_9.setText(_translate("MainWindow", "Control Knobs"))
        self.label_10.setText(_translate("MainWindow", "1-Bit                    Prediction:\nBranch Predictor     Hit/Miss:"))
        self.label_11.setText(_translate("MainWindow", "Block Diagram of Instructions"))
        self.label_8.setText(_translate("MainWindow", "Clock:"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">           PC                Instructions</p></body></html>"))
        # new stuff
        self.label.adjustSize()
        self.label_2.adjustSize()
        self.label_3.adjustSize()
        self.label_4.adjustSize()
        self.label_5.adjustSize()
        self.label_6.adjustSize()
        self.label_7.adjustSize()
        self.label_9.adjustSize()
        self.label_10.adjustSize()
        self.label_11.adjustSize()
        self.checkBox.adjustSize()
        self.radioBox_2.adjustSize()
        self.radioBox_3.adjustSize()
        self.checkBox_4.adjustSize()
        self.pushButton_7.adjustSize()
        self.pushButton_2.clicked.connect(lambda: self.opendata())
        self.pushButton_7.clicked.connect(lambda: self.buffers())
        self.pushButton.clicked.connect(lambda: self.guihelp())
        self.pushButton_4.clicked.connect(lambda: self.outputlog())
        self.pushButton_6.clicked.connect(lambda: self.assembly())
        self.pushButton_5.clicked.connect(lambda: self.step())
        self.pushButton_3.clicked.connect(lambda: self.run())
        self.checkBox.clicked.connect(lambda: self.pipelining())
    def buffers(self):
        tempx=""
        nice=self.varlist[-1]
        keys=self.lineEdit.text()
        if(nice.get(str(keys),-1)!=-1):
            for x in nice[str(keys)]:
                tempx+=(str(x)+" is "+str(nice[str(keys)][x])+"\n")
        else:
            tempx="This Instruction does not exist\n"
        data=open("output.txt",'a')
        data.write(tempx)
        data.write("\n\n")
        self.textBrowser.append(tempx)
        if(self.checkBox_4.isChecked()):
            tempx=""
            for x in nice:
                for y in nice[x]:
                    tempx+=(str(y)+" is "+str(nice[x][y])+"\n")
            data=open("output.txt",'a')
            data.write(tempx)
            data.write("\n\n")
            self.textBrowser.append(tempx)


        

    def pipelining(self):
        if(self.pipeline):
            self.pipeline=0
            self.radioBox_2.setHidden(True)
            self.radioBox_3.setHidden(True)
            self.checkBox.setStyleSheet("background-color : red")
        else:
            self.radioBox_2.setHidden(False)
            self.radioBox_3.setHidden(False)
            self.pipeline=1
            self.checkBox.setStyleSheet("background-color : green")

    def opendata(self):
        try:
            string=os.path.abspath(os.getcwd())
            string+="\data.mc"
            os.startfile(string)
        except:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, "data.mc"])
    def guihelp(self):
        try:
            string=os.path.abspath(os.getcwd())
            string+="\README.md"
            os.startfile(string)
        except:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, "README.md"])
    def outputlog(self):
        try:
            string=os.path.abspath(os.getcwd())
            string+="\output.txt"
            os.startfile(string)
        except:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, "output.txt"])
    def assembly(self):
        if(self.pipeline):
            if(self.radioBox_3.isChecked()):
                self.tableWidget_4.clear()
                self.reg,self.idi,self.dd,self.clock,self.varlist=gui_forwarding.assemble()
                self.loaddata(self.reg)
                self.loaddata2(self.idi)
                self.loaddata3(self.dd)
                self.pc=self.varlist[0]
                self.outtext=self.varlist[17]
                self.bdd=self.varlist[16]
                mem_pc=self.varlist[7]
                write_pc=self.varlist[8]
                execute_pc=self.varlist[9]
                decode_pc=self.varlist[10]
                fetch_pc=self.varlist[11]
                self.cpc=[fetch_pc[:],decode_pc[:],execute_pc[:],mem_pc[:],write_pc[:]]
                
                self.loaddata4(self.bdd,self.cpc)
                
                self.textBrowser_3.clear()
                self.textBrowser_3.append("Pipelined Execution")
                self.textBrowser_4.clear()
                self.textBrowser_4.append("Pipelined Execution")
                self.clockadj()
                self.tableWidget_2.clear()
                self.textBrowser.clear()
                
                data=open("output.txt","wt")
                data.write("")
            else:
                self.reg,self.idi,self.dd,self.clock,self.varlist=gui_stalling.assemble()
                self.tableWidget_4.clear()
                self.loaddata(self.reg)
                self.loaddata2(self.idi)
                self.loaddata3(self.dd)
                self.pc=self.varlist[0]
                self.outtext=self.varlist[20]
                self.bdd=self.varlist[19]
                mem_pc=self.varlist[7]
                write_pc=self.varlist[8]
                execute_pc=self.varlist[9]
                decode_pc=self.varlist[10]
                fetch_pc=self.varlist[11]
                self.cpc=[fetch_pc[:],decode_pc[:],execute_pc[:],mem_pc[:],write_pc[:]]
                
                self.loaddata4(self.bdd,self.cpc)
                self.textBrowser_3.clear()
                self.textBrowser_3.append("Pipelined Execution")
                self.textBrowser_4.clear()
                self.textBrowser_4.append("Pipelined Execution")
                self.clockadj()
                self.tableWidget_2.clear()
                self.textBrowser.clear()
                data=open("output.txt","wt")
                data.write("")

        else:
            self.cachesize=int(self.lineEdit_2.text())
            self.blocksize=int(self.lineEdit_3.text())
            self.sa_ways=int(self.lineEdit_4.text())
            self.input_list=[self.cachesize,self.blocksize,self.sa_ways]
            print(self.input_list)
            self.ir,self.pc,self.reg,self.idi,self.dd,self.clock,self.pc_f,self.pc_t,self.cache_list=gui_main.assemble(self.input_list) 
            self.loaddata(self.reg)
            self.loaddata2(self.idi)
            self.loaddata3(self.dd)
            self.textBrowser_3.clear()
            self.textBrowser_3.append(self.pc)
            self.tableWidget_4.clear()
            self.textBrowser_4.clear()
            self.clockadj()
            self.tableWidget_2.clear()
            self.textBrowser.clear()
            data=open("output.txt","wt")
            data.write("")

    def step(self):
        if(self.pipeline):
            if(self.radioBox_3.isChecked()):
                if(self.pc!=-1):
                    self.reg,self.idi,self.dd,self.clock,self.varlist=gui_forwarding.runstep(self.reg,self.idi,self.dd,self.clock,self.varlist)
                    self.loaddata(self.reg)
                    self.loaddata2(self.idi)
                    self.loaddata3(self.dd)
                    self.pc=self.varlist[0]
                    self.outtext=self.varlist[17]
                    self.bdd=self.varlist[16]
                    mem_pc=self.varlist[7]
                    write_pc=self.varlist[8]
                    execute_pc=self.varlist[9]
                    decode_pc=self.varlist[10]
                    fetch_pc=self.varlist[11]
                    self.cpc=[fetch_pc[:],decode_pc[:],execute_pc[:],mem_pc[:],write_pc[:]]
                    
                    self.loaddata4(self.bdd,self.cpc)
                    
                    self.clockadj()
                    self.textBrowser.append(self.outtext)
                    data=open("output.txt",'a')
                    if(self.pc==-1):
                        data.write("X----------------X\nCode Ran Successfully\n")
                    data.write(self.outtext)
                    data.write("\n\n")
                else:
                    self.outtext=gui_forwarding.runstep(self.reg,self.idi,self.dd,self.clock,self.varlist)
                    data=open("output.txt",'a')
                    data.write(self.outtext)
                    data.write("\n\n")
                    self.textBrowser.append(self.outtext)
                    return
            else:
                if(self.pc!=-1):
                    self.reg,self.idi,self.dd,self.clock,self.varlist=gui_stalling.runstep(self.reg,self.idi,self.dd,self.clock,self.varlist)
                    self.loaddata(self.reg)
                    self.loaddata2(self.idi)
                    self.loaddata3(self.dd)
                    self.pc=self.varlist[0]
                    self.outtext=self.varlist[20]
                    self.bdd=self.varlist[19]
                    mem_pc=self.varlist[7]
                    write_pc=self.varlist[8]
                    execute_pc=self.varlist[9]
                    decode_pc=self.varlist[10]
                    fetch_pc=self.varlist[11]
                    self.cpc=[fetch_pc[:],decode_pc[:],execute_pc[:],mem_pc[:],write_pc[:]]
                    
                    self.loaddata4(self.bdd,self.cpc)
                    
                    self.clockadj()
                    self.textBrowser.append(self.outtext)
                    data=open("output.txt",'a')
                    if(self.pc==-1):
                        data.write("X----------------X\nCode Ran Successfully\n")
                    data.write(self.outtext)
                    data.write("\n\n")
                else:
                    self.outtext=gui_forwarding.runstep(self.reg,self.idi,self.dd,self.clock,self.varlist)
                    data=open("output.txt",'a')
                    data.write(self.outtext)
                    data.write("\n\n")
                    self.textBrowser.append(self.outtext)
                    return
        else:
            if(self.pc!=-1):
                num=int(self.pc,16)
                temp_pc=self.pc
                self.idi,self.pc,self.pc_f,self.pc_t,self.reg,self.dd,self.ir,self.clock,self.outtext,self.cache_list=gui_main.runstep(self.idi,self.pc,self.pc_f,self.pc_t,self.reg,self.dd,self.ir,self.clock,self.cache_list)
                self.loaddata(self.reg)
                self.loaddata2(self.idi)
                self.loaddata3(self.dd)
                if(self.pc!=-1):
                    self.tableWidget_3.item(num//4,0).setBackground(QtGui.QColor(18,243,78))
                    self.tableWidget_3.item(num//4,1).setBackground(QtGui.QColor(18,243,78))
                    self.tableWidget_3.scrollToItem(self.tableWidget_3.item(num//4, 0))
                else:
                    num=int(temp_pc,16)
                    self.tableWidget_3.item(num//4-1,0).setBackground(QtGui.QColor(255,111,0))
                    self.tableWidget_3.item(num//4-1,1).setBackground(QtGui.QColor(255,111,0))
                    self.tableWidget_3.scrollToItem(self.tableWidget_3.item(num//4-1, 0))

                self.textBrowser_3.clear()
                if(self.pc!=-1):
                    self.textBrowser_3.append(str(self.pc))
                else:
                    self.textBrowser_3.append("Completed")
                self.textBrowser_4.clear()
                self.textBrowser_4.append(self.ir)
                self.clockadj()
                self.textBrowser.append(self.outtext)
                data=open("output.txt",'a')
                data.write("PC is "+str(self.pc)+"\nIR is "+str(self.ir)+"\n")
                if(self.pc==-1):
                    data.write("X----------------X\nCode Ran Successfully\n")
                data.write(self.outtext)
                data.write("\n\n")
            else:
                self.outtext=gui_stalling.runstep(self.reg,self.idi,self.dd,self.clock,self.varlist)
                data=open("output.txt",'a')
                data.write(self.outtext)
                data.write("\n\n")
                self.textBrowser.append(self.outtext)
                return
    def run(self):
        if(self.pipeline):
            if(self.radioBox_3.isChecked()):
                while(self.pc!=-1):
                    self.reg,self.idi,self.dd,self.clock,self.varlist=gui_forwarding.runstep(self.reg,self.idi,self.dd,self.clock,self.varlist)
                    self.loaddata(self.reg)
                    self.loaddata2(self.idi)
                    self.loaddata3(self.dd)
                    self.pc=self.varlist[0]
                    self.outtext=self.varlist[17]
                    self.bdd=self.varlist[16]
                    mem_pc=self.varlist[7]
                    write_pc=self.varlist[8]
                    execute_pc=self.varlist[9]
                    decode_pc=self.varlist[10]
                    fetch_pc=self.varlist[11]
                    self.cpc=[fetch_pc[:],decode_pc[:],execute_pc[:],mem_pc[:],write_pc[:]]
                    self.loaddata4(self.bdd,self.cpc)
                    self.clockadj()
                    self.textBrowser.append(self.outtext)
                    data=open("output.txt",'a')
                    if(self.pc==-1):
                        
                        data.write("X----------------X\nCode Ran Successfully\n")
                    data.write(self.outtext)
                    data.write("\n\n")
                self.outtext=gui_forwarding.runstep(self.reg,self.idi,self.dd,self.clock,self.varlist)
                data=open("output.txt",'a')
                data.write(self.outtext)
                data.write("\n\n")
                self.textBrowser.append(self.outtext)
            else:
                while(self.pc!=-1):
                    self.reg,self.idi,self.dd,self.clock,self.varlist=gui_stalling.runstep(self.reg,self.idi,self.dd,self.clock,self.varlist)
                    self.loaddata(self.reg)
                    self.loaddata2(self.idi)
                    self.loaddata3(self.dd)
                    self.pc=self.varlist[0]
                    self.outtext=self.varlist[20]
                    self.bdd=self.varlist[19]
                    mem_pc=self.varlist[7]
                    write_pc=self.varlist[8]
                    execute_pc=self.varlist[9]
                    decode_pc=self.varlist[10]
                    fetch_pc=self.varlist[11]
                    self.cpc=[fetch_pc[:],decode_pc[:],execute_pc[:],mem_pc[:],write_pc[:]]
                    self.loaddata4(self.bdd,self.cpc)
                    self.clockadj()
                    self.textBrowser.append(self.outtext)
                    data=open("output.txt",'a')
                    if(self.pc==-1):
                        
                        data.write("X----------------X\nCode Ran Successfully\n")
                    data.write(self.outtext)
                    data.write("\n\n")
                self.outtext=gui_stalling.runstep(self.reg,self.idi,self.dd,self.clock,self.varlist)
                data=open("output.txt",'a')
                data.write(self.outtext)
                data.write("\n\n")
                self.textBrowser.append(self.outtext)
        else:
            while(self.pc!=-1):
                num=int(self.pc,16)
                temp_pc=self.pc
                self.idi,self.pc,self.pc_f,self.pc_t,self.reg,self.dd,self.ir,self.clock,self.outtext,self.cache_list=gui_main.runstep(self.idi,self.pc,self.pc_f,self.pc_t,self.reg,self.dd,self.ir,self.clock,self.cache_list)
                self.loaddata(self.reg)
                self.loaddata2(self.idi)
                self.loaddata3(self.dd)
                if(self.pc!=-1):
                    self.tableWidget_3.item(num//4,0).setBackground(QtGui.QColor(18,243,78))
                    self.tableWidget_3.item(num//4,1).setBackground(QtGui.QColor(18,243,78))
                    self.tableWidget_3.scrollToItem(self.tableWidget_3.item(num//4, 0))
                else:
                    num=int(temp_pc,16)
                    
                    self.tableWidget_3.item(num//4-1,0).setBackground(QtGui.QColor(255,111,0))
                    self.tableWidget_3.item(num//4-1,1).setBackground(QtGui.QColor(255,111,0))
                    self.tableWidget_3.scrollToItem(self.tableWidget_3.item(num//4-1, 0))
                self.textBrowser_3.clear()

                if(self.pc!=-1):
                    self.textBrowser_3.append(str(self.pc))
                else:
                    self.textBrowser_3.append("Completed")
                self.textBrowser_4.clear()
                self.textBrowser_4.append(self.ir)
                self.clockadj()
                self.textBrowser.append(self.outtext)
                data=open("output.txt",'a')
                data.write("PC is "+str(self.pc)+"\nIR is "+str(self.ir)+"\n")
                if(self.pc==-1):
                    data.write("X----------------X\nCode Ran Successfully\n")
                data.write(self.outtext)
                data.write("\n\n")
        

    def clockadj(self):
        self.textBrowser_6.clear()
        temp1=""
        temp=5
        if(self.pipeline):
            temp=1
        if(self.clock==1):
            temp1=str(self.clock*temp)+" Cycles"
        else:
            temp1=str(self.clock*temp)+ " Cycles"
        self.textBrowser_6.append(temp1)
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())