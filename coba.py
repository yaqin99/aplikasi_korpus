from PyQt5 import QtCore, QtGui, QtWidgets
from addData import Ui
from daftar_kata import Daftar
from ringkasan import Ringkasan
from single import Single
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



class Ui_MainWindow(object):

    panjang = 0
    
    def ngeprint(self):
        theId =  self.tableWidget.selectedItems()[0]
        korpus = ''
        
            
        cursorB.execute("SELECT * FROM meta_data WHERE id_korpus = " + theId.text())
        for a in cursorB : 
            judul = a[7]
            penulis = a[8]
            kategori = a[9]
            penerbit = a[4]
            sumber = a[3]
            tanggal = a[2]
            cursorA.execute("SELECT konten FROM korpus WHERE id_korpus =" + theId.text())
            for x in cursorA:
                korpus = x[0]
                    
        self.window = QtWidgets.QMainWindow()
        self.ui = Single()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.isi_judul.setText(judul)
        self.ui.isi_kategori.setText(kategori)
        self.ui.isi_penerbit.setText(penerbit)
        self.ui.isi_pengarang.setText(penulis)
        self.ui.isi_sumber.setText(sumber)
        self.ui.isi_tanggal.setText(str(tanggal))
        self.ui.isi_korpus.setText(korpus)

    def inputForm(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui()
        self.ui.setupUi(self.window)
        self.window.show()

    def daftar_kata(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Daftar()
        self.ui.setupUi(self.window)
        self.window.show()

    def ringkasan(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ringkasan()
        self.ui.setupUi(self.window)
        self.window.show()

    
        

    def showText(self):
        
        global panjang
        row = 0
        sql = self.textEdit.toPlainText() 
        combo = self.comboBox.currentText() 
        self.tableWidget.clear()
        
        cursorC.execute("SELECT * FROM korpus WHERE konten LIKE "+"'"+"%"+sql+"%"+"'")
        panjang = len(cursorC.fetchall())
       
        cursorA.execute("SELECT * FROM korpus WHERE konten LIKE "+"'"+"%"+sql+"%"+"'")
        for y in cursorA:
            id_korpus = y[0] 
            if combo == 'Pilih Kategori':
                print("tanpa kategori")
                cursorB.execute("SELECT * FROM meta_data WHERE id_korpus = " +str(id_korpus))
                for a in cursorB:
                    id_nya = a[1]
                    judul = a[7]
                    penulis = a[8]
                    kategori = a[9]
                    penerbit = a[4]
                    sumber = a[3]
                    tanggal = a[2]
                    self.tableWidget.setColumnCount(7)
                    self.tableWidget.setHorizontalHeaderLabels(('id','Judul','Penulis','Kategori','Penerbit','Sumber','Tanggal'))
                    self.tableWidget.setRowCount(panjang)
                    self.tableWidget.setColumnWidth(0,200)
                    self.tableWidget.setColumnWidth(1,200)
                    self.tableWidget.setColumnWidth(2,200)
                    self.tableWidget.setColumnWidth(3,200)
                    self.tableWidget.setColumnWidth(4,200)
                    self.tableWidget.setColumnWidth(5,200)
                    self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(str(id_nya)))
                    self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(judul))
                    self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(penulis))
                    self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(kategori))
                    self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(penerbit))
                    self.tableWidget.setItem(row,5,QtWidgets.QTableWidgetItem(sumber))
                    self.tableWidget.setItem(row,6,QtWidgets.QTableWidgetItem(str(tanggal)))
                    # item = self.tableWidget.item(row, 1)
                    # item_text = item.text()
                    # self.tableWidget.cellClicked.connect(lambda : self.ngeprint(item_text))
                    row += 1 

            elif combo != 'Pilih Kategori':  
                print("dengan kategori")  
                db2 = "SELECT * FROM meta_data WHERE id_korpus = " +str(id_korpus) + " AND " + "kategori = "+ "'" + combo + "'" ; 
                cursorB.execute(db2)
                for a in cursorB:
                    id_nya = a[1]
                    judul = a[7]
                    penulis = a[8]
                    kategori = a[9]
                    penerbit = a[4]
                    sumber = a[3]
                    tanggal = a[2]
                    self.tableWidget.setColumnCount(6)
                    self.tableWidget.setHorizontalHeaderLabels(('Judul','Penulis','Kategori','Penerbit','Sumber','Tanggal'))
                    self.tableWidget.setRowCount(panjang)
                    self.tableWidget.setColumnWidth(0,200)
                    self.tableWidget.setColumnWidth(1,200)
                    self.tableWidget.setColumnWidth(2,200)
                    self.tableWidget.setColumnWidth(3,200)
                    self.tableWidget.setColumnWidth(4,200)
                    self.tableWidget.setColumnWidth(5,200)
                    self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(judul))
                    self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(penulis))
                    self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(kategori))
                    self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(penerbit))
                    self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(sumber))
                    self.tableWidget.setItem(row,5,QtWidgets.QTableWidgetItem(str(tanggal)))
                    row += 1 
              
        db.commit()
        

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 589)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.showText())
        self.pushButton.setGeometry(QtCore.QRect(450, 80, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 10, 291, 71))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(220, 80, 221, 31))
        self.textEdit.setObjectName("textEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(220, 130, 151, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Pilih Kategori")
        self.comboBox.addItem("Teks Narasi")
        self.comboBox.addItem("Teks Deskripsi")
        self.comboBox.addItem("Teks Eksplanasi")
        self.comboBox.addItem("Teks Eksposisi")
        self.comboBox.addItem("Teks Prosedur")
        self.comboBox.addItem("Teks Anekdot")
        self.comboBox.addItem("Teks Laporan")
        self.comboBox.addItem("Teks Berita")
        self.comboBox.addItem("Teks Normatif")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(110, 180, 581, 331))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 21))
        self.menubar.setObjectName("menubar")
        self.menuInput = QtWidgets.QMenu(self.menubar)
        self.menuInput.setObjectName("menuInput")
        self.menuInput_2 = QtWidgets.QMenu(self.menubar)
        self.menuInput_2.setObjectName("menuInput_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDaftar_Kata = QtWidgets.QAction(MainWindow)
        self.actionDaftar_Kata.setObjectName("actionDaftar_Kata")
        self.actionInput = QtWidgets.QAction(MainWindow)
        self.actionInput.setObjectName("actionInput")
        self.actionHome = QtWidgets.QAction(MainWindow)
        self.actionHome.setObjectName("actionHome")
        self.actionRingkasan = QtWidgets.QAction(MainWindow)
        self.actionRingkasan.setObjectName("actionRingkasan")
        self.actionDaftar_Kata_2 = QtWidgets.QAction(MainWindow)
        self.actionDaftar_Kata_2.setObjectName("actionDaftar_Kata_2")
        self.menuInput.addAction(self.actionRingkasan)
        self.menuInput.addAction(self.actionDaftar_Kata_2)
        self.menuInput_2.addAction(self.actionInput)
        self.menubar.addAction(self.menuInput.menuAction())
        self.menubar.addAction(self.menuInput_2.menuAction())
        self.actionInput.triggered.connect(lambda:self.inputForm())
        self.actionDaftar_Kata_2.triggered.connect(lambda:self.daftar_kata())
        self.actionRingkasan.triggered.connect(lambda:self.ringkasan())
        self.tableWidget.cellClicked.connect(lambda:self.ngeprint())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Cari "))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Silahkan Masukan Korpus</span></p></body></html>"))
        self.menuInput.setTitle(_translate("MainWindow", "Main"))
        self.menuInput_2.setTitle(_translate("MainWindow", "Form"))
        self.actionDaftar_Kata.setText(_translate("MainWindow", "Daftar Kata"))
        self.actionInput.setText(_translate("MainWindow", "Input"))
        self.actionRingkasan.setText(_translate("MainWindow", "Unduh Korpus"))
        self.actionDaftar_Kata_2.setText(_translate("MainWindow", "Daftar Kata"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    sys.exit(app.exec_())
