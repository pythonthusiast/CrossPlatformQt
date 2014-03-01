from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QDialog, QMessageBox
from ui_logindialog import Ui_LoginDialog
from auth import Auth

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

class LoginDialog(QDialog, Ui_LoginDialog):
    Success,Failed,Rejected = range(0,3)
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.onAccept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.onReject)

    def onAccept(self):

        auth = Auth()
        if auth.doLogin(self.txtUsername.text(), self.txtPassword.text()):
            self.setResult(self.Success)
        else:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle(_translate("LoginDialog", "Pythonthusiast", None))
            msgBox.setText(_translate("LoginDialog", "Either incorrect username and/or password. Try again!", None))
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            self.setResult(self.Failed)

    def onReject(self):
        self.setResult(self.Rejected)





