# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Feb 27 17:02:42 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(334, 125)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 334, 22))
        self.menuBar.setNativeMenuBar(False)
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menu_File = QtGui.QMenu(self.menuBar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_Help = QtGui.QMenu(self.menuBar)
        self.menu_Help.setObjectName(_fromUtf8("menu_Help"))
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionE_xit = QtGui.QAction(MainWindow)
        self.actionE_xit.setMenuRole(QtGui.QAction.ApplicationSpecificRole)
        self.actionE_xit.setObjectName(_fromUtf8("actionE_xit"))
        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setMenuRole(QtGui.QAction.AboutRole)
        self.action_About.setObjectName(_fromUtf8("action_About"))
        self.menu_File.addAction(self.actionE_xit)
        self.menu_Help.addAction(self.action_About)
        self.menuBar.addAction(self.menu_File.menuAction())
        self.menuBar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menu_File.setTitle(_translate("MainWindow", "&File", None))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help", None))
        self.actionE_xit.setText(_translate("MainWindow", "E&xit", None))
        self.action_About.setText(_translate("MainWindow", "&About", None))

import app_rc
