# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logindialog.ui'
#
# Created: Thu Feb 20 15:54:38 2014
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

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName(_fromUtf8("LoginDialog"))
        LoginDialog.resize(266, 139)
        self.buttonBox = QtGui.QDialogButtonBox(LoginDialog)
        self.buttonBox.setGeometry(QtCore.QRect(90, 100, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(LoginDialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(LoginDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtPassword = QtGui.QLineEdit(LoginDialog)
        self.txtPassword.setGeometry(QtCore.QRect(80, 60, 161, 23))
        self.txtPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.txtPassword.setObjectName(_fromUtf8("txtPassword"))
        self.txtUsername = QtGui.QLineEdit(LoginDialog)
        self.txtUsername.setGeometry(QtCore.QRect(80, 20, 161, 23))
        self.txtUsername.setObjectName(_fromUtf8("txtUsername"))

        self.retranslateUi(LoginDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), LoginDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), LoginDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)
        LoginDialog.setTabOrder(self.txtUsername, self.txtPassword)
        LoginDialog.setTabOrder(self.txtPassword, self.buttonBox)

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Dialog", None))
        self.label.setText(_translate("LoginDialog", "Username", None))
        self.label_2.setText(_translate("LoginDialog", "Password", None))

