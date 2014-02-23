# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logindialog.ui'
#
# Created: Sun Feb 23 20:51:24 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(266, 139)
        self.buttonBox = QtGui.QDialogButtonBox(LoginDialog)
        self.buttonBox.setGeometry(QtCore.QRect(90, 100, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtGui.QLabel(LoginDialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(LoginDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 61, 16))
        self.label_2.setObjectName("label_2")
        self.txtPassword = QtGui.QLineEdit(LoginDialog)
        self.txtPassword.setGeometry(QtCore.QRect(80, 60, 161, 23))
        self.txtPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.txtPassword.setObjectName("txtPassword")
        self.txtUsername = QtGui.QLineEdit(LoginDialog)
        self.txtUsername.setGeometry(QtCore.QRect(80, 20, 161, 23))
        self.txtUsername.setObjectName("txtUsername")

        self.retranslateUi(LoginDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), LoginDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), LoginDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)
        LoginDialog.setTabOrder(self.txtUsername, self.txtPassword)
        LoginDialog.setTabOrder(self.txtPassword, self.buttonBox)

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(QtGui.QApplication.translate("LoginDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("LoginDialog", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("LoginDialog", "Password", None, QtGui.QApplication.UnicodeUTF8))

