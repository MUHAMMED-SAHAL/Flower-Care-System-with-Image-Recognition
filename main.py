import sys
from mainscreen import Ui_Dialog
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QFileDialog
from testing import *
import mysql.connector as mysql

mydb = mysql.connect(host='localhost', user='root', passwd='sahal@1234', database='cnn')
mycursor = mydb.cursor()


class MainWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.instructions = None
        self.fname = None
        self.pixmap = None
        self.prediction = None
        self.setupUi(self)
        self.browse.clicked.connect(self.openFile)

    def printf(self):
        print(self.fname)

    def openFile(self):
        self.fname = QFileDialog.getOpenFileName(self, "Open Files", r"C:\Users\Sahal\FLOWERS RECOGNITION\Prediction",
                                                 "All Files (*)")
        self.pixmap = QPixmap(self.fname[0])
        self.ImageLabel.setPixmap(self.pixmap)
        self.printf()
        self.prediction = predict(self.fname[0])
        self.plantRecognized.setText(
            "Plant Recognized: " + self.prediction[0].capitalize())
        try:
            mycursor.execute("SELECT * FROM flower WHERE flower_name = %s", (self.prediction[0],))
            self.instructions = mycursor.fetchall()[0]
            self.water.setPlainText(self.instructions[2])
            self.sunlight.setPlainText(self.instructions[3])
            self.soil.setPlainText(self.instructions[4])
        except Exception as e:
            print(f"Exception: {e}")


app = QApplication(sys.argv)
welcome = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.setFixedWidth(1200)
widget.setFixedHeight(800)
widget.addWidget(welcome)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
