from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QGraphicsBlurEffect ,QFontDialog
from PyQt5.QtCore import QTimer
from ping_ui import Ui_MainWindow
import sys
import configparser
from configparser import NoOptionError

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

    # name_list = open("config_files/hostname.txt").read().splitlines()
    # name_code = open("config_files/hostname_code.txt").read().splitlines()

    def __init__(self):
        super(MyWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # self.ui.setWindowIcon(QtGui.QIcon('logo.png')) 
        self.ui.actionResult_Font_Size.triggered.connect(self.font_result)
        self.ui.actionHostname_Code_Size.triggered.connect(self.font_label_code)
        self.ui.actionFull_Screen.triggered.connect(self.showFullScreen)
        self.ui.actionNormal_Screen.triggered.connect(self.showNormal)
        self.ui.action3_Screen.triggered.connect(self.hide_dashboard)
        self.ui.action6_Screen.triggered.connect(self.showall_dashboard)

        self.config = configparser.ConfigParser()
        self.config.read('config_files/config.ini')
        
        try:
            self.host1_ip = self.config['host1']['ipaddress']
            self.host1_name = self.config['host1']['hostname']
            self.host1_code = self.config['host1']['host_code']
            
            self.host2_ip = self.config['host2']['ipaddress']
            self.host2_name = self.config['host2']['hostname']
            self.host2_code = self.config['host2']['host_code']

            self.host3_ip = self.config['host3']['ipaddress']
            self.host3_name = self.config['host3']['hostname']
            self.host3_code = self.config['host3']['host_code']

            self.host4_ip =self.config['host4']['ipaddress']
            self.host4_name = self.config['host4']['hostname']
            self.host4_code = self.config['host4']['host_code']

            self.host5_ip = self.config['host5']['ipaddress']
            self.host5_name = self.config['host5']['hostname']
            self.host5_code = self.config['host5']['host_code']

            self.host6_ip = self.config['host6']['ipaddress']
            self.host6_name = self.config['host6']['hostname']
            self.host6_code = self.config['host6']['host_code']

            self.font_code = QtGui.QFont()
            self.font_code.setPointSize(60)
            self.ui.label1.setFont(self.font_code)
            self.ui.label1.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.label1.setText(self.host1_code)
            self.ui.label1.setStyleSheet("background-color: green") 

            self.ui.label2.setFont(self.font_code)
            self.ui.label2.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.label2.setText(self.host2_code)
            self.ui.label2.setStyleSheet("background-color: green")

            self.ui.label3.setFont(self.font_code)
            self.ui.label3.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.label3.setText(self.host3_code)
            self.ui.label3.setStyleSheet("background-color: green")

            self.ui.label4.setFont(self.font_code)
            self.ui.label4.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.label4.setText(self.host4_code)
            self.ui.label4.setStyleSheet("background-color: green")

            self.ui.label5.setFont(self.font_code)
            self.ui.label5.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.label5.setText(self.host5_code)
            self.ui.label5.setStyleSheet("background-color: green")

            self.ui.label6.setFont(self.font_code)
            self.ui.label6.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.label6.setText(self.host6_code)
            self.ui.label6.setStyleSheet("background-color: green")

        except KeyError:
            pass

        self.font = QtGui.QFont()
        self.font.setPointSize(8)
        self.ui.plaintxt1.setFont(self.font)
        self.ui.plaintxt2.setFont(self.font)
        self.ui.plaintxt3.setFont(self.font)
        self.ui.plaintxt4.setFont(self.font)
        self.ui.plaintxt5.setFont(self.font)
        self.ui.plaintxt6.setFont(self.font)

        self.ui.label1.adjustSize()
        self.ui.label2.adjustSize()
        self.ui.label3.adjustSize()
        self.ui.label4.adjustSize()
        self.ui.label5.adjustSize()
        self.ui.label6.adjustSize()


        self.font_ms= QtGui.QFont()
        self.font_ms.setPointSize(36)
        self.ui.ms1.setFont(self.font_ms)
        self.ui.ms1.setAlignment(QtCore.Qt.AlignCenter)

        self.ui.ms2.setFont(self.font_ms)
        self.ui.ms2.setAlignment(QtCore.Qt.AlignCenter)

        self.ui.ms3.setFont(self.font_ms)
        self.ui.ms3.setAlignment(QtCore.Qt.AlignCenter)

        self.ui.ms4.setFont(self.font_ms)
        self.ui.ms4.setAlignment(QtCore.Qt.AlignCenter)

        self.ui.ms5.setFont(self.font_ms)
        self.ui.ms5.setAlignment(QtCore.Qt.AlignCenter)

        self.ui.ms6.setFont(self.font_ms)
        self.ui.ms6.setAlignment(QtCore.Qt.AlignCenter)

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


    def font_result(self):
        font, ok = QFontDialog.getFont(self)
        if ok:
            self.ui.plaintxt1.setFont(font)
            self.ui.plaintxt2.setFont(font)
            self.ui.plaintxt3.setFont(font)
            self.ui.plaintxt4.setFont(font)
            self.ui.plaintxt5.setFont(font)
            self.ui.plaintxt6.setFont(font)
            # print("Display Fonts", font)

    def font_label_code(self):
        font_code, ok = QFontDialog.getFont(self)
        if ok:
            self.ui.label1.setFont(font_code)
            self.ui.label2.setFont(font_code)
            self.ui.label3.setFont(font_code)
            self.ui.label4.setFont(font_code)
            self.ui.label5.setFont(font_code)
            self.ui.label6.setFont(font_code)
            # print("Display Fonts", font)

    def hide_dashboard(self):
        self.ui.label4.hide()
        self.ui.label5.hide()
        self.ui.label6.hide()
        self.ui.plaintxt4.hide()
        self.ui.plaintxt5.hide()
        self.ui.plaintxt6.hide()
        self.ui.ms4.hide()
        self.ui.ms5.hide()
        self.ui.ms6.hide()

    def showall_dashboard(self):
        self.ui.label4.show()
        self.ui.label5.show()
        self.ui.label6.show()
        self.ui.plaintxt4.show()
        self.ui.plaintxt5.show()
        self.ui.plaintxt6.show()
        self.ui.ms4.show()
        self.ui.ms5.show()
        self.ui.ms6.show()

    

    
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

        try:
            result = result1.split()

            if str(result[4]) == "time<1ms":
                ping_result = str(result[4]).replace("time<","")
            else:
                ping_result = str(result[4]).replace("time=","")

            self.ui.ms1.setText(ping_result)
        except IndexError:
            pass
        
        if "Request timed out." in result1:
            self.ui.label1.setStyleSheet("background-color: red")
            self.ui.plaintxt1.setStyleSheet("background-color: red")
            self.ui.plaintxt1.appendPlainText(f"{self.host1_name} --> RTO")

            self.ui.ms1.setStyleSheet("background-color: red")
            self.ui.ms1.setText("RTO")

        elif "Destination host unreachable." in result1:
            self.ui.label1.setStyleSheet("background-color: red")
            self.ui.plaintxt1.setStyleSheet("background-color: red")
            self.ui.plaintxt1.appendPlainText(f"{self.host1_name} --> UNREACHABLE")

            self.ui.ms1.setStyleSheet("background-color: red")
            self.ui.ms1.setText("Unreachable")

        elif "General failure." in result1:
            self.ui.label1.setStyleSheet("background-color: red")
            self.ui.plaintxt1.setStyleSheet("background-color: red")
            self.ui.plaintxt1.appendPlainText(f"{self.host1_name} --> General Failure")

            self.ui.ms1.setStyleSheet("background-color: red")
            self.ui.ms1.setText("Failure")
        else:
            self.ui.plaintxt1.setStyleSheet("background-color: black")
            self.ui.label1.setStyleSheet("background-color: green")
            self.ui.ms1.setStyleSheet("background-color: black")
            
    
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
        
        try:
            result = result2.split()

            if str(result[4]) == "time<1ms":
                ping_result = str(result[4]).replace("time<","")
            else:
                ping_result = str(result[4]).replace("time=","")

            self.ui.ms2.setText(ping_result)

        except IndexError:
            pass

        if "Request timed out." in result2:
            self.ui.label2.setStyleSheet("background-color: red")
            self.ui.plaintxt2.setStyleSheet("background-color: red")
            self.ui.plaintxt2.appendPlainText(f"{self.host2_name} --> RTO")

            self.ui.ms2.setStyleSheet("background-color: red")
            self.ui.ms2.setText("RTO")

        elif "Destination host unreachable." in result2:
            self.ui.label2.setStyleSheet("background-color: red")
            self.ui.plaintxt2.setStyleSheet("background-color: red")
            self.ui.plaintxt2.appendPlainText(f"{self.host2_name} --> UNREACHABLE")

            self.ui.ms2.setStyleSheet("background-color: red")
            self.ui.ms2.setText("Unreachable")

        elif "General failure." in result2:
            self.ui.label2.setStyleSheet("background-color: red")
            self.ui.plaintxt2.setStyleSheet("background-color: red")
            self.ui.plaintxt2.appendPlainText(f"{self.host2_name} --> General Failure")

            self.ui.ms2.setStyleSheet("background-color: red")
            self.ui.ms2.setText("Failure")

        else:
            self.ui.plaintxt2.setStyleSheet("background-color: black")
            self.ui.label2.setStyleSheet("background-color: green") 
            self.ui.ms2.setStyleSheet("background-color: black")
    
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

        try:
            result = result3.split()
            if str(result[4]) == "time<1ms":
                ping_result = str(result[4]).replace("time<","")
            else:
                ping_result = str(result[4]).replace("time=","")
            
            self.ui.ms3.setText(ping_result)
        
        except IndexError:
            pass

        if "Request timed out." in result3:
            self.ui.label3.setStyleSheet("background-color: red")
            self.ui.plaintxt3.setStyleSheet("background-color: red") 
            self.ui.plaintxt3.appendPlainText(f"{self.host3_name} --> RTO")

            self.ui.ms3.setStyleSheet("background-color: red")
            self.ui.ms3.setText("RTO")

        elif "Destination host unreachable." in result3:
            self.ui.label3.setStyleSheet("background-color: red")
            self.ui.plaintxt3.setStyleSheet("background-color: red")
            self.ui.plaintxt3.appendPlainText(f"{self.host3_name} --> UNREACHABLE")

            self.ui.ms3.setStyleSheet("background-color: red")
            self.ui.ms3.setText("Unreachable")

        elif "General failure." in result3:
            self.ui.label3.setStyleSheet("background-color: red")
            self.ui.plaintxt3.setStyleSheet("background-color: red")
            self.ui.plaintxt3.appendPlainText(f"{self.host3_name} --> General Failure")

            self.ui.ms3.setStyleSheet("background-color: red")
            self.ui.ms3.setText("Failure")
        else:
            self.ui.plaintxt3.setStyleSheet("background-color: black") 
            self.ui.label3.setStyleSheet("background-color: green")
            self.ui.ms3.setStyleSheet("background-color: black")
    
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

        try:
            result = result4.split()
            if str(result[4]) == "time<1ms":
                ping_result = str(result[4]).replace("time<","")
            else:
                ping_result = str(result[4]).replace("time=","")
            self.ui.ms4.setText(ping_result)

        except IndexError:
            pass

        if "Request timed out." in result4:
            self.ui.label4.setStyleSheet("background-color: red")
            self.ui.plaintxt4.setStyleSheet("background-color: red") 
            self.ui.plaintxt4.appendPlainText(f"{self.host4_name} --> RTO")

            self.ui.ms4.setStyleSheet("background-color: red")
            self.ui.ms4.setText("RTO")

        elif "Destination host unreachable." in result4:
            self.ui.label4.setStyleSheet("background-color: red")
            self.ui.plaintxt4.setStyleSheet("background-color: red")
            self.ui.plaintxt4.appendPlainText(f"{self.host4_name} --> UNREACHABLE")

            self.ui.ms4.setStyleSheet("background-color: red")
            self.ui.ms4.setText("Unreachable")

        elif "General failure." in result4:
            self.ui.label4.setStyleSheet("background-color: red")
            self.ui.plaintxt4.setStyleSheet("background-color: red")
            self.ui.plaintxt4.appendPlainText(f"{self.host4_name} --> General Failure")
            
            self.ui.ms4.setStyleSheet("background-color: red")
            self.ui.ms4.setText("Failure")
            
        else:
            self.ui.plaintxt4.setStyleSheet("background-color: black") 
            self.ui.label4.setStyleSheet("background-color: green")
            self.ui.ms4.setStyleSheet("background-color: black")
    
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

        try:
            result = result5.split()
            
            if str(result[4]) == "time<1ms":
                ping_result = str(result[4]).replace("time<","")
            else:
                ping_result = str(result[4]).replace("time=","")

            self.ui.ms5.setText(ping_result)
            # self.ui.label1.setText(result[4])
        except IndexError:
            pass

        if "Request timed out." in result5:
            self.ui.label5.setStyleSheet("background-color: red")
            self.ui.plaintxt5.setStyleSheet("background-color: red")
            self.ui.plaintxt5.appendPlainText(f"{self.host5_name} --> RTO")

            self.ui.ms5.setStyleSheet("background-color: red")
            self.ui.ms5.setText("RTO")

        elif "Destination host unreachable." in result5:
            self.ui.label5.setStyleSheet("background-color: red")
            self.ui.plaintxt5.setStyleSheet("background-color: red")
            self.ui.plaintxt5.appendPlainText(f"{self.host5_name} --> UNREACHABLE")

            self.ui.ms5.setStyleSheet("background-color: red")
            self.ui.ms5.setText("Unreachable")
        
        elif "General failure." in result5:
            self.ui.label5.setStyleSheet("background-color: red")
            self.ui.plaintxt5.setStyleSheet("background-color: red")
            self.ui.plaintxt5.appendPlainText(f"{self.host5_name} --> General Failure")

            self.ui.ms5.setStyleSheet("background-color: red")
            self.ui.ms5.setText("Failure")

        else:
            self.ui.plaintxt5.setStyleSheet("background-color: black") 
            self.ui.label5.setStyleSheet("background-color: green")
            self.ui.ms5.setStyleSheet("background-color: black")
    
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

        try:
            result = result6.split()
                        
            if str(result[4]) == "time<1ms":
                ping_result = str(result[4]).replace("time<","")
            else:
                ping_result = str(result[4]).replace("time=","")

            self.ui.ms6.setText(ping_result)
            # self.ui.label1.setText(result[4])
        except IndexError:
            pass

        if "Request timed out." in result6:
            self.ui.label6.setStyleSheet("background-color: red")
            self.ui.plaintxt6.setStyleSheet("background-color: red")
            self.ui.plaintxt6.appendPlainText(f"{self.host6_name} --> RTO")

            self.ui.ms6.setStyleSheet("background-color: red")
            self.ui.ms6.setText("RTO")

        elif "Destination host unreachable." in result6:
            self.ui.label6.setStyleSheet("background-color: red")
            self.ui.plaintxt6.setStyleSheet("background-color: red")
            self.ui.plaintxt6.appendPlainText(f"{self.host6_name} --> UNREACHABLE")

            self.ui.ms6.setStyleSheet("background-color: red")
            self.ui.ms6.setText("Unreachable")

        elif "General failure." in result6:
            self.ui.label6.setStyleSheet("background-color: red")
            self.ui.plaintxt6.setStyleSheet("background-color: red")
            self.ui.plaintxt6.appendPlainText(f"{self.host6_name} --> General Failure")
            
            self.ui.ms6.setStyleSheet("background-color: red")
            self.ui.ms6.setText("Failure")
        else:
            self.ui.plaintxt6.setStyleSheet("background-color: black") 
            self.ui.label6.setStyleSheet("background-color: green")
            self.ui.ms6.setStyleSheet("background-color: black")
            
    
    def run6(self, command):
        self.ui.plaintxt6.clear()
        self.process6.start(command)
########################################################################################################################
def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    w = MyWindow()
    w.setWindowIcon(QtGui.QIcon('logo.ico')) 
    w.show()

    try:
        w.run1(f"ping {w.host1_ip} -t")
        w.run2(f"ping {w.host2_ip} -t")
        w.run3(f"ping {w.host3_ip} -t")
        w.run4(f"ping {w.host4_ip} -t")
        w.run5(f"ping {w.host5_ip} -t")
        w.run6(f"ping {w.host6_ip} -t")

    except AttributeError:
        pass

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