from PyQt5 import QtCore, QtGui, QtWidgets

from addData import Ui
from PyQt5.QtWidgets import QMainWindow , QApplication , QPushButton , QFileDialog
import sys
import mysql.connector

db = mysql.connector.connect(
    host="localhost" , 
    user="root",
    password = "" , 
    database = "korpus" , 
)


cursorA = db.cursor(buffered=True)
cursorB = db.cursor(buffered=True)
cursorC = db.cursor(buffered=True)



class Daftar(object):

    def inputForm(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui()
        self.ui.setupUi(self.window)
        self.window.show()

    def daftar_kata(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui()
        self.ui.setupUi(self.window)
        self.window.show()

    def getData(self):
        self.listWidget.clear()
        sql = self.textEdit.toPlainText()  

        cursorA.execute("SELECT * FROM daftar_kata WHERE nama_kata LIKE "+"'"+"%"+sql+"%"+"'")
        number = 1
        for a in cursorA:
            self.listWidget.addItem(str(number)+ ". " + a[1])
            number += 1

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(230, 80, 221, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked =  lambda : self.getData())
        self.pushButton.setGeometry(QtCore.QRect(460, 80, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 10, 251, 71))
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(230, 140, 331, 401))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        self.menuForm = QtWidgets.QMenu(self.menubar)
        self.menuForm.setObjectName("menuForm")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionRingkasan = QtWidgets.QAction(MainWindow)
        self.actionRingkasan.setObjectName("actionRingkasan")
        self.actionDaftar_Kata = QtWidgets.QAction(MainWindow)
        self.actionDaftar_Kata.setObjectName("actionDaftar_Kata")
        self.actionInput = QtWidgets.QAction(MainWindow)
        self.actionInput.setObjectName("actionInput")
        self.menuMain.addAction(self.actionRingkasan)
        self.menuMain.addAction(self.actionDaftar_Kata)
        self.menuForm.addAction(self.actionInput)
        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuForm.menuAction())
        self.actionInput.triggered.connect(lambda:self.inputForm())
        self.actionInput.triggered.connect(lambda:self.daftar_kata())
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Cari "))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Silahkan Masukan Kata</span></p></body></html>"))
        self.menuMain.setTitle(_translate("MainWindow", "Main"))
        self.menuForm.setTitle(_translate("MainWindow", "Form"))
        self.actionRingkasan.setText(_translate("MainWindow", "Unduh Korpus"))
        self.actionDaftar_Kata.setText(_translate("MainWindow", "Daftar Kata"))
        self.actionInput.setText(_translate("MainWindow", "Input"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = QtWidgets.QMainWindow()
    ui = Daftar()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
