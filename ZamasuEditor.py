#
# Author : Petruknisme
# Site: https://Petruknisme.com
# License : GPLv2
# Modified from this
# http://kib2.free.fr/tutos/PyQt4/QScintilla2.html
# http://eli.thegreenplace.net/2011/04/01/sample-using-qscintilla-with-pyqt
# Thanks to Kib and Eli Bendersky (eliben@gmail.com)
#
# Zamasu Search is a Python GUI Based for Searching Exploit from exploit-database repository
# https://github.com/aancw/ZamasuSearch.git
#

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.Qsci import *

class ZamasuEditor_Window(QsciScintilla):
    def __init__(self, fileName=None, parent=None):
        super(ZamasuEditor_Window, self).__init__(parent)

        self.setWindowTitle("ZamasuEditor - " + fileName )
        self.setMinimumSize(800, 768)
        ## define the font to use
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setFixedPitch(True)
        font.setPointSize(10)

        # the font metrics here will help
        # building the margin width later
        fm = QtGui.QFontMetrics(font)

        ## set the default font of the editor
        ## and take the same font for line numbers
        self.setFont(font)
        self.setMarginsFont(font)

        ## Folding visual : we will use boxes
        self.setFolding(QsciScintilla.BoxedTreeFoldStyle)

        ## Braces matching
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)

        # folding margin colors (foreground,background)
        self.setFoldMarginColors(QtGui.QColor("#99CC66"),QtGui.QColor("#333300"))

        ## Line numbers
        # conventionnaly, margin 0 is for line numbers
        self.setMarginWidth(0, fm.width( "00000" ) + 5)
        self.setMarginLineNumbers(0, True)

        #fileName = "exploit-database/platforms/arm/shellcode/15314.asm"
        file_extension = os.path.splitext(fileName)[1]

        """
            We need to define Lexer same as File Extensions :)
        """
        if file_extension == ".py":
            lexer = QsciLexerPerl()
        elif file_extension == ".rb":
            lexer = QsciLexerRuby()
        elif file_extension == ".c" or file_extension == ".cpp":
            lexer = QsciLexerCPP()
        elif file_extension == ".sh":
            lexer = QsciLexerBash()
        elif file_extension == ".pl":
            lexer = QsciLexerPerl()
        elif file_extension == ".html" or file_extension == ".htm":
            lexer = QsciLexerHTML()
        elif file_extension == ".lua":
            lexer = QsciLexerLua()
        else:
            lexer = QsciLexerPython() # Why Python? I think lexer python is good :D

        lexer.setDefaultFont(font)
        self.setLexer(lexer)

        self.setAutoCompletionThreshold(1)
        self.setWrapMode(QsciScintilla.WrapWord)

        ## Tell the editor we are using a QsciAPI for the autocompletion
        self.setAutoCompletionSource(QsciScintilla.AcsAPIs)
        self.setText(open(fileName).read())

if __name__ == "__main__":
    app = QApplication()
    editor = ZamasuEditor_Window()
    editor.show()
    app.exec_()
