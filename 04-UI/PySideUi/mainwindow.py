from PySide import QtCore, QtGui
from PySide.QtGui import QApplication, QMainWindow, QMessageBox, QPixmap
from ui_mainwindow import Ui_MainWindow
import res

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.actionE_xit.triggered.connect(self.onExit)
        self.action_About.triggered.connect(self.onAbout)

    def onExit(self):
        msgBox = QMessageBox(self)
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setWindowTitle(_translate("MainWindow", "Pythonthusiast", None));
        msgBox.setText(_translate("MainWindow", "Are you sure you want to quit?", None))
        msgBox.setStandardButtons(QMessageBox.No|QMessageBox.Yes)
        msgBox.setDefaultButton(QMessageBox.Yes)
        msgBox.exec_
        if msgBox.exec_() == QMessageBox.Yes:
          QtGui.qApp.quit()

    def onAbout(self):
        msgBox = QMessageBox(self)
        msgBox.setIconPixmap(QPixmap(":/images/sherlock.png"))
        msgBox.setWindowTitle(_translate("MainWindow", "Pythonthusiast", None))
        msgBox.setText(_translate("MainWindow", "Well Watson, isn't it obvious to you that Qt rocks?", None))
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()
