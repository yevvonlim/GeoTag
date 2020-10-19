import os
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QWidget, QMessageBox
from PyQt5 import QtGui
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

form = uic.loadUiType(os.getcwd() + "\\mainUI.ui")[0]
class MyWindow(QMainWindow, form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('ico.png'))
        self.btn_getdata.clicked.connect(self.btn1_clicked)

    def btn1_clicked(self):
        directory = os.getcwd() + "\\images"
        extensions = [".png", ".jpg", ".jpeg"]
        images = get_filelist(directory, extensions)
        f = open(os.getcwd()+"/failed_to_load.txt", "w")
        f.write("This is a list of files that does not contain GPS information.\n\n")

        for failed in make_excel(images):
            f.write(failed+"\n")
        f.close()
        QMessageBox.about(self, "Confirm", "All Done!.")

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()


   
