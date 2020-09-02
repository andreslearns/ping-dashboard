from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QGraphicsBlurEffect
from PyQt5.QtCore import QTimer
from ping_ui import Ui_MainWindow

import sys
import subprocess as sp

class MyWindow(QtWidgets.QMainWindow):

    errorSignal1 = QtCore.pyqtSignal(str) 
    outputSignal1 = QtCore.pyqtSignal(str)

    errorSignal2 = QtCore.pyqtSignal(str) 
    outputSignal2 = QtCore.pyqtSignal(str)

    errorSignal3 = QtCore.pyqtSignal(str) 
    outputSignal3 = QtCore.pyqtSignal(str)

    errorSignal4 = QtCore.pyqtSignal(str) 
    outputSignal4 = QtCore.pyqtSignal(str)

    errorSignal5 = QtCore.pyqtSignal(str) 
    outputSignal5 = QtCore.pyqtSignal(str)

    errorSignal6 = QtCore.pyqtSignal(str) 
    outputSignal6 = QtCore.pyqtSignal(str)

    name_list = open("hosts/hostname.txt").read().splitlines()

    def __init__(self):
        super(MyWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.font = QtGui.QFont()
        self.font.setPointSize(8)
        self.ui.plaintxt1.setFont(self.font)
        self.ui.plaintxt2.setFont(self.font)
        self.ui.plaintxt3.setFont(self.font)
        self.ui.plaintxt4.setFont(self.font)
        self.ui.plaintxt5.setFont(self.font)
        self.ui.plaintxt6.setFont(self.font)

        self.ui.plaintxt1.adjustSize()
        self.ui.plaintxt2.adjustSize()
        self.ui.plaintxt3.adjustSize()
        self.ui.plaintxt4.adjustSize()
        self.ui.plaintxt5.adjustSize()
        self.ui.plaintxt6.adjustSize()


########################################################################################################################
        self.output1 = None
        self.error1 = None

        self.output2 = None
        self.error2 = None

        self.output3 = None
        self.error3 = None

        self.output4 = None
        self.error4 = None

        self.output5 = None
        self.error5 = None

        self.output6 = None
        self.error6 = None

########################################################################################################################
        self.process1 = QtCore.QProcess()
        self.process1.readyReadStandardError.connect(self.onReadyReadStandardError1)
        self.process1.readyReadStandardOutput.connect(self.onReadyReadStandardOutput1)

        self.process2 = QtCore.QProcess()
        self.process2.readyReadStandardError.connect(self.onReadyReadStandardError2)
        self.process2.readyReadStandardOutput.connect(self.onReadyReadStandardOutput2)

        self.process3 = QtCore.QProcess()
        self.process3.readyReadStandardError.connect(self.onReadyReadStandardError3)
        self.process3.readyReadStandardOutput.connect(self.onReadyReadStandardOutput3)

        self.process4 = QtCore.QProcess()
        self.process4.readyReadStandardError.connect(self.onReadyReadStandardError4)
        self.process4.readyReadStandardOutput.connect(self.onReadyReadStandardOutput4)

        self.process5 = QtCore.QProcess()
        self.process5.readyReadStandardError.connect(self.onReadyReadStandardError5)
        self.process5.readyReadStandardOutput.connect(self.onReadyReadStandardOutput5)

        self.process6 = QtCore.QProcess()
        self.process6.readyReadStandardError.connect(self.onReadyReadStandardError6)
        self.process6.readyReadStandardOutput.connect(self.onReadyReadStandardOutput6)

        print(self.name_list)

########################################################################################################################
    #107.154.26.52 
    def onReadyReadStandardError1(self):
        error1 = self.process1.readAllStandardError().data().decode()
        self.ui.plaintxt1.appendPlainText(error1)
        self.errorSignal1.emit(error1)

    def onReadyReadStandardOutput1(self):
        result1 = self.process1.readAllStandardOutput().data().decode()
        self.ui.plaintxt1.appendPlainText(result1)
        self.outputSignal1.emit(result1)

        if "Request timed out." in result1:
            self.ui.plaintxt1.setStyleSheet("background-color: red")
            self.ui.plaintxt1.appendPlainText(f"{self.name_list[0]} --> RTO")

        elif "Destination host unreachable." in result1:
            self.ui.plaintxt1.setStyleSheet("background-color: red")
            self.ui.plaintxt1.appendPlainText(f"{self.name_list[0]} --> UNREACHABLE")

        elif "General failure." in result1:
            self.ui.plaintxt1.setStyleSheet("background-color: red")
            self.ui.plaintxt1.appendPlainText(f"{self.name_list[0]} --> General Failure")
        else:
            self.ui.plaintxt1.setStyleSheet("background-color: black") 

    
    def run1(self, command):
        self.ui.plaintxt1.clear()
        self.process1.start(command)

########################################################################################################################
    #107.154.33.5
    def onReadyReadStandardError2(self):
        error2 = self.process2.readAllStandardError().data().decode()
        self.ui.plaintxt2.appendPlainText(error2)
        self.errorSignal2.emit(error2)

    def onReadyReadStandardOutput2(self):
        result2 = self.process2.readAllStandardOutput().data().decode()
        self.ui.plaintxt2.appendPlainText(result2)
        self.outputSignal2.emit(result2)

        if "Request timed out." in result2:
            self.ui.plaintxt2.setStyleSheet("background-color: red")
            self.ui.plaintxt2.appendPlainText(f"{self.name_list[1]} --> RTO")

        elif "Destination host unreachable." in result2:
            self.ui.plaintxt2.setStyleSheet("background-color: red")
            self.ui.plaintxt2.appendPlainText(f"{self.name_list[1]} --> UNREACHABLE")

        elif "General failure." in result2:
            self.ui.plaintxt2.setStyleSheet("background-color: red")
            self.ui.plaintxt2.appendPlainText(f"{self.name_list[1]} --> General Failure")

        else:
            self.ui.plaintxt2.setStyleSheet("background-color: black") 
    
    def run2(self, command):
        self.ui.plaintxt2.clear()
        self.process2.start(command)

########################################################################################################################
    #120.89.30.28
    def onReadyReadStandardError3(self):
        error3 = self.process3.readAllStandardError().data().decode()
        self.ui.plaintxt3.appendPlainText(error3)
        self.errorSignal3.emit(error3)

    def onReadyReadStandardOutput3(self):
        result3 = self.process3.readAllStandardOutput().data().decode()
        self.ui.plaintxt3.appendPlainText(result3)
        self.outputSignal3.emit(result3)

        if "Request timed out." in result3:
            self.ui.plaintxt3.setStyleSheet("background-color: red") 
            self.ui.plaintxt3.appendPlainText(f"{self.name_list[2]} --> RTO")

        elif "Destination host unreachable." in result3:
            self.ui.plaintxt3.setStyleSheet("background-color: red")
            self.ui.plaintxt3.appendPlainText(f"{self.name_list[2]} --> UNREACHABLE")

        elif "General failure." in result3:
            self.ui.plaintxt3.setStyleSheet("background-color: red")
            self.ui.plaintxt3.appendPlainText(f"{self.name_list[2]} --> General Failure")
        else:
            self.ui.plaintxt3.setStyleSheet("background-color: black") 
    
    def run3(self, command):
        self.ui.plaintxt3.clear()
        self.process3.start(command)

########################################################################################################################
    #203.177.110.117
    def onReadyReadStandardError4(self):
        error4 = self.process4.readAllStandardError().data().decode()
        self.ui.plaintxt4.appendPlainText(error4)
        self.errorSignal4.emit(error4)

    def onReadyReadStandardOutput4(self):
        result4 = self.process4.readAllStandardOutput().data().decode()
        self.ui.plaintxt4.appendPlainText(result4)
        self.outputSignal3.emit(result4)

        if "Request timed out." in result4:
            self.ui.plaintxt4.setStyleSheet("background-color: red") 
            self.ui.plaintxt4.appendPlainText(f"{self.name_list[3]} --> RTO")

        elif "Destination host unreachable." in result4:
            self.ui.plaintxt4.setStyleSheet("background-color: red")
            self.ui.plaintxt4.appendPlainText(f"{self.name_list[3]} --> UNREACHABLE")

        elif "General failure." in result4:
            self.ui.plaintxt4.setStyleSheet("background-color: red")
            self.ui.plaintxt4.appendPlainText(f"{self.name_list[3]} --> General Failure")
        else:
            self.ui.plaintxt4.setStyleSheet("background-color: black") 
    
    def run4(self, command):
        self.ui.plaintxt4.clear()
        self.process4.start(command)

########################################################################################################################
    #121.58.215.186 - CONVERGE
    def onReadyReadStandardError5(self):
        error5 = self.process5.readAllStandardError().data().decode()
        self.ui.plaintxt5.appendPlainText(error5)
        self.errorSignal5.emit(error5)

    def onReadyReadStandardOutput5(self):
        result5 = self.process5.readAllStandardOutput().data().decode()
        self.ui.plaintxt5.appendPlainText(result5)
        self.outputSignal5.emit(result5)

        if "Request timed out." in result5:
            self.ui.plaintxt5.setStyleSheet("background-color: red")
            self.ui.plaintxt5.appendPlainText(f"{self.name_list[4]} --> RTO")

        elif "Destination host unreachable." in result5:
            self.ui.plaintxt5.setStyleSheet("background-color: red")
            self.ui.plaintxt5.appendPlainText(f"{self.name_list[4]} --> UNREACHABLE")
        
        elif "General failure." in result5:
            self.ui.plaintxt5.setStyleSheet("background-color: red")
            self.ui.plaintxt5.appendPlainText(f"{self.name_list[4]} --> General Failure")

        else:
            self.ui.plaintxt5.setStyleSheet("background-color: black") 
    
    def run5(self, command):
        self.ui.plaintxt5.clear()
        self.process5.start(command)

########################################################################################################################
    #172.16.255.253 # CLOUDWARE
    def onReadyReadStandardError6(self):
        error6 = self.process6.readAllStandardError().data().decode()
        self.ui.plaintxt6.appendPlainText(error6)
        self.errorSignal6.emit(error6)

    def onReadyReadStandardOutput6(self):
        result6 = self.process6.readAllStandardOutput().data().decode()
        self.ui.plaintxt6.appendPlainText(result6)
        self.outputSignal6.emit(result6)

        if "Request timed out." in result6:
            self.ui.plaintxt6.setStyleSheet("background-color: red")
            self.ui.plaintxt6.appendPlainText(f"{self.name_list[5]} --> RTO")

        elif "Destination host unreachable." in result6:
            self.ui.plaintxt6.setStyleSheet("background-color: red")
            self.ui.plaintxt6.appendPlainText(f"{self.name_list[5]} --> UNREACHABLE")

        elif "General failure." in result6:
            self.ui.plaintxt6.setStyleSheet("background-color: red")
            self.ui.plaintxt6.appendPlainText(f"{self.name_list[5]} --> General Failure")
        else:
            self.ui.plaintxt6.setStyleSheet("background-color: black") 
            
    
    def run6(self, command):
        self.ui.plaintxt6.clear()
        self.process6.start(command)
########################################################################################################################



def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    w = MyWindow()
    w.show()
    host_list = open("hosts/ipaddress.txt").read().splitlines()
    w.run1(f"ping {host_list[0]} -t")
    w.run2(f"ping {host_list[1]} -t")
    w.run3(f"ping {host_list[2]} -t")
    w.run4(f"ping {host_list[3]} -t")
    w.run5(f"ping {host_list[4]} -t")
    w.run6(f"ping {host_list[5]} -t")
    sys.exit(app.exec_())




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53,53,53))
    palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(15,15,15))
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53,53,53))
    palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53,53,53))
    palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
         
    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(142,45,197).lighter())
    palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    app.setPalette(palette)
    main()