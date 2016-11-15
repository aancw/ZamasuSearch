##############################################
# Author : Petruknisme
# Site: https://Petruknisme.com
# License : GPLv2
# Zamasu Search is a Python GUI Based for Searching Exploit from exploit-database repository
# https://github.com/aancw/ZamasuSearch.git
##############################################

import sys, os, subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout
from PyQt5.QtCore import QProcess

class ZamasuUpdater_Window(QWidget):
    def __init__(self, updateMode=None, parent=None):
        super(ZamasuUpdater_Window, self).__init__(parent)
        self.setWindowTitle("Zamasu Updater")

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

        if updateMode == "init":
            self.process.start('git',['clone', 'https://github.com/offensive-security/exploit-database.git', '--progress'])
        elif updateMode == "update" and self.checkExistFolder("exploit-database"):
            self.process.setWorkingDirectory("exploit-database")
            self.process.start('git',['pull', '--progress'])

        #self.process.started.connect(self.startEvent)
        self.process.readyReadStandardOutput.connect(self.stdoutReady)
        self.process.readyReadStandardError.connect(self.stderrReady)
        self.process.finished.connect(self.finishEvent)

    def checkExistFolder(self, folderName):
        if os.path.isdir(folderName):
            return True

    def stdoutReady(self):
        text = str(self.process.readAllStandardOutput())
        self.text.clear()
        self.text.append(text)
    def stderrReady(self):
        text = str(self.process.readAllStandardError())
        self.text.clear()
        self.text.setText(text)
    #def startEvent(self):
    def finishEvent(self):
        QtWidgets.QMessageBox.about(self, "Info", "Update finish!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    updater = ZamasuUpdater_Window()
    updater.show()
    app.exec_()
