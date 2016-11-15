#
# Author : Petruknisme
# Site: https://Petruknisme.com
# License : GPLv2
# Zamasu Search is a Python GUI Based for Searching Exploit from exploit-database repository
# https://github.com/aancw/ZamasuSearch.git
#

from PyQt5 import QtCore, QtGui, QtWidgets
import csv, os, sys
from PyQt5.QtWidgets import QApplication, QAbstractItemView, QMessageBox
from PyQt5.Qsci import *
from ZamasuEditor import ZamasuEditor_Window
from ZamasuUpdater import ZamasuUpdater_Window
from ZamasuAbout import ZamasuAbout_Window

class Ui_MainZamasu(object):
    def setupUi(self, MainZamasu):
        MainZamasu.setObjectName("MainZamasu")
        MainZamasu.setMinimumSize(QtCore.QSize(872, 600))
        self.centralwidget = QtWidgets.QWidget(MainZamasu)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, -30, 421, 111))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 80, 151, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 120, 151, 18))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 160, 151, 18))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 200, 151, 18))
        self.label_5.setObjectName("label_5")
        self.cmbPlatform = QtWidgets.QComboBox(self.centralwidget)
        self.cmbPlatform.setGeometry(QtCore.QRect(120, 160, 161, 32))
        self.cmbPlatform.setObjectName("cmbPlatform")
        self.cmbPlatform.addItem("")
        self.cmbType = QtWidgets.QComboBox(self.centralwidget)
        self.cmbType.setGeometry(QtCore.QRect(120, 200, 161, 32))
        self.cmbType.setObjectName("cmbType")
        self.cmbType.addItem("")
        self.txtDesc = QtWidgets.QTextEdit(self.centralwidget)
        self.txtDesc.setGeometry(QtCore.QRect(120, 70, 450, 31))
        self.txtDesc.setObjectName("txtDesc")
        self.txtAuthor = QtWidgets.QTextEdit(self.centralwidget)
        self.txtAuthor.setGeometry(QtCore.QRect(120, 120, 251, 31))
        self.txtAuthor.setObjectName("txtAuthor")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 330, 851, 221))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.btnSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearch.setGeometry(QtCore.QRect(600, 280, 241, 34))
        self.btnSearch.setObjectName("btnSearch")
        self.btnUpdateDb = QtWidgets.QPushButton(self.centralwidget)
        self.btnUpdateDb.setGeometry(QtCore.QRect(600, 70, 241, 111))
        self.btnUpdateDb.setObjectName("btnUpdateDb")
        self.andMode = QtWidgets.QCheckBox(self.centralwidget)
        self.andMode.setGeometry(QtCore.QRect(120, 290, 88, 22))
        self.andMode.setObjectName("andMode")
        self.orMode = QtWidgets.QCheckBox(self.centralwidget)
        self.orMode.setGeometry(QtCore.QRect(210, 290, 88, 22))
        self.orMode.setObjectName("orMode")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 290, 151, 18))
        self.label_7.setObjectName("label_7")
        self.caseMode = QtWidgets.QCheckBox(self.centralwidget)
        self.caseMode.setGeometry(QtCore.QRect(290, 290, 141, 22))
        self.caseMode.setObjectName("caseMode")
        MainZamasu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainZamasu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 877, 30))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainZamasu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainZamasu)
        self.statusbar.setObjectName("statusbar")
        MainZamasu.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainZamasu)
        QtCore.QMetaObject.connectSlotsByName(MainZamasu)

        self.btnSearch.clicked.connect(self.searchExploit)
        self.btnUpdateDb.clicked.connect(self.updateDatabase)
        self.andMode.setChecked(True)
        self.tableWidget.resizeRowsToContents()

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        #self.tableWidget.verticalHeader().sectionClicked.connect(self.tableClickedEvent)
        self.tableWidget.cellDoubleClicked.connect(self.tableClickedEvent)

        if not self.checkExistFolder("exploit-database"):
            reply = QMessageBox.question(MainZamasu, "Warning", "Database folder not found. Update database?",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                self.updater = ZamasuUpdater_Window("init")
                self.updater.show()
        else:
            """ Load Data from CSV and add item to combobox """
            self.loadPlatformData()
            self.loadTypeData()

    def slotAbout(self):
      print(" is triggered")

    def tableClickedEvent(self, row, column):
        fileNameLocation = self.tableWidget.item(self.tableWidget.currentRow(), 7).text()
        if column == 7:
            # Open new window for text editor
            if self.checkExistFolder("exploit-database"):
                self.openEditor("exploit-database/" + fileNameLocation)

    def openEditor(self, fileNameLocation):
        self.editor = ZamasuEditor_Window(fileNameLocation)
        self.editor.show()

    def checkExistFolder(self, folderName):
        if os.path.isdir(folderName):
            return True

    def loadPlatformData(self):
        if self.getCSVRowsGroupBy("platform") is not None:
            for ls in self.getCSVRowsGroupBy("platform"):
                self.cmbPlatform.addItem(ls)

    def loadTypeData(self):
        if self.getCSVRowsGroupBy("platform") is not None:
            for ls in self.getCSVRowsGroupBy("type"):
                self.cmbType.addItem(ls)

    def getCSVRowsGroupBy(self, rowName):
        if self.checkExistFolder("exploit-database"):
            with open("exploit-database/files.csv") as f_obj:
                reader = csv.DictReader(f_obj, delimiter=',')
                rowList = set([line[rowName] for line in reader])
                return rowList

    def searchExploit(self):
        mDesc = self.txtDesc.toPlainText()
        mAuthor = self.txtAuthor.toPlainText()
        mPlatform = self.cmbPlatform.currentText()
        mType = self.cmbType.currentText()
        mANDMode = self.andMode.isChecked()
        mORMode = self.orMode.isChecked()
        caseMode = self.caseMode.isChecked()
        self.clearTable()
        if self.checkExistFolder("exploit-database"):
            with open("exploit-database/files.csv") as f_obj:
                reader = csv.DictReader(f_obj, delimiter=',')
                for line in reader:
                    nId = line["id"]
                    nDesc = line["description"]
                    nAuthor = line["author"]
                    nDate = line["date"]
                    nPlatform = line["platform"]
                    nType = line["type"]
                    nPort = line["port"]
                    nFile = line["file"]

                    if not caseMode:
                        nDescReal = nDesc
                        nAuthorReal = nAuthor
                        nDesc = nDesc.lower()
                        nAuthor = nAuthor.lower()
                        mDesc = mDesc.lower()
                        mAuthor = mAuthor.lower()
                    else:
                        nDescReal = nDesc
                        nAuthorReal = nAuthor

                    if mANDMode and mORMode:
                        QtWidgets.QMessageBox.about(MainZamasu, "Info", "Can't search with 2 parameter, please choose AND or OR mode")
                    elif mANDMode:
                        """
                            We need separate search category with 2 phase, i think Platform and type is optional.
                            This logic is bad(?) . I just want more accurate searching :)
                        """
                        # Searching only with Desc and Author
                        if (mDesc != "" or mAuthor != "") and (mPlatform == "Any Platform" and mType == "Any Type"):
                            if mDesc == nDesc and mAuthor == nAuthor:
                                self.addDataToRows(nId, nDescReal, nDate, nAuthorReal, nPlatform, nType, nPort, nFile)
                            elif mDesc != "" and mAuthor == "" and mDesc == nDesc:
                                self.addDataToRows(nId, nDescReal, nDate, nAuthorReal, nPlatform, nType, nPort, nFile)
                            elif mAuthor != "" and mDesc == "" and mAuthor == nAuthor:
                                self.addDataToRows(nId, nDescReal, nDate, nAuthorReal, nPlatform, nType, nPort, nFile)

                        # Search Desc and Author with Platform and Type
                        if mDesc != "" or mAuthor != "" and (mPlatform != "Any Platform" or mType != "Any Type"):
                            if mDesc != "" and (mPlatform != "Any Platform" or mType != "Any Type"):
                                if mPlatform != "Any Platform" and mType == "Any Type" and (mDesc == nDesc and mPlatform == nPlatform):
                                    QtWidgets.QMessageBox.about(MainZamasu, "Info", "2A1")
                                    self.addDataToRows(nId, nDescReal, nDate, nAuthorReal, nPlatform, nType, nPort, nFile)
                                if mType != "Any Type" and mPlatform == "Any Platform" and (mDesc == nDesc and mType == nType):
                                    QtWidgets.QMessageBox.about(MainZamasu, "Info", "2A2")
                                    self.addDataToRows(nId, nDescReal, nDate, nAuthorReal, nPlatform, nType, nPort, nFile)
                                if mType != "Any Type" and mPlatform != "Any Platform" and (mDesc == nDesc and mType == nType and mPlatform == nPlatform):
                                    QtWidgets.QMessageBox.about(MainZamasu, "Info", "2A3")
                                    self.addDataToRows(nId, nDescReal, nDate, nAuthorReal, nPlatform, nType, nPort, nFile)

                            elif mAuthor != "" and (mPlatform != "Any Platform" or mType != "Any Type"):
                                if mPlatform != "Any Platform" and (mAuthor == nAuthor and mPlatform == nPlatform):
                                    QtWidgets.QMessageBox.about(MainZamasu, "Info", "2B1")
                                    self.addDataToRows(nId, nDescReal, nDate, nAuthorReal, nPlatform, nType, nPort, nFile)
                                if mType != "Any Type" and (mAuthor == nAuthor and mType == nType):
                                    QtWidgets.QMessageBox.about(MainZamasu, "Info", "2B2")
                                    self.addDataToRows(nId, nDescReal, nDate, nAuthorReal, nPlatform, nType, nPort, nFile)

    def clearTable(self):
        self.tableWidget.setRowCount(0)

    def addDataToRows(self, idItem, desc, date, author, platform, typeExploit, port, fileLocation):
        # Automatic add row position number
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)

        self.tableWidget.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(idItem))
        self.tableWidget.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(desc))
        self.tableWidget.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(date))
        self.tableWidget.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(author))
        self.tableWidget.setItem(rowPosition , 4, QtWidgets.QTableWidgetItem(platform))
        self.tableWidget.setItem(rowPosition , 5, QtWidgets.QTableWidgetItem(typeExploit))
        self.tableWidget.setItem(rowPosition , 6, QtWidgets.QTableWidgetItem(port))
        self.tableWidget.setItem(rowPosition , 7, QtWidgets.QTableWidgetItem(fileLocation))

    def updateDatabase(self):
        reply = QMessageBox.question(MainZamasu, "Warning", "Update Database now?",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            self.updater = ZamasuUpdater_Window("update")
            self.updater.show()

    def retranslateUi(self, MainZamasu):
        _translate = QtCore.QCoreApplication.translate
        MainZamasu.setWindowTitle(_translate("MainZamasu", "Zamasu Search"))
        self.label.setText(_translate("MainZamasu", "Zamasu Search"))
        self.label_2.setText(_translate("MainZamasu", "Description/Title :"))
        self.label_3.setText(_translate("MainZamasu", "Author :"))
        self.label_4.setText(_translate("MainZamasu", "Platform :"))
        self.label_5.setText(_translate("MainZamasu", "Type :"))
        self.cmbPlatform.setItemText(0, _translate("MainZamasu", "Any Platform"))
        self.cmbType.setItemText(0, _translate("MainZamasu", "Any Type"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainZamasu", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainZamasu", "Description"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainZamasu", "Date"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainZamasu", "Author"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainZamasu", "Platform"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainZamasu", "Type"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainZamasu", "Port"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainZamasu", "File"))
        self.btnSearch.setText(_translate("MainZamasu", "Search"))
        self.btnUpdateDb.setText(_translate("MainZamasu", "UPDATE DATABASE"))
        self.andMode.setText(_translate("MainZamasu", "AND"))
        self.orMode.setText(_translate("MainZamasu", "OR"))
        self.label_7.setText(_translate("MainZamasu", "Search Mode:"))
        self.caseMode.setText(_translate("MainZamasu", "Case Sensitive"))
        self.menuAbout.setTitle(_translate("MainZamasu", "Abo&ut"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainZamasu = QtWidgets.QMainWindow()
    ui = Ui_MainZamasu()
    ui.setupUi(MainZamasu)
    MainZamasu.show()
    sys.exit(app.exec_())
