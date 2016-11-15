#
# Author : Petruknisme
# Site: https://Petruknisme.com
# License : GPLv2
# Zamasu Search is a Python GUI Based for Searching Exploit from exploit-database repository
# https://github.com/aancw/ZamasuSearch.git
#

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout
from PyQt5.QtCore import QProcess

class ZamasuAbout_Window(QWidget):
    def __init__(self, parent=None):
        super(ZamasuAbout_Window, self).__init__(parent)
        self.setWindowTitle("Zamasu About")

        ## define the font to use
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setFixedPitch(True)
        font.setPointSize(10)

        self.text = QtWidgets.QTextEdit(self)
        self.process = QProcess(self)

        layout = QVBoxLayout(self)
        layout.addWidget(self.text)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    about = ZamasuAbout_Window()
    about.show()
    app.exec_()
