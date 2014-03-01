import sip
sip.setapi("QString", 2)

import sys
from PyQt4.QtGui import QApplication
from logindialog import LoginDialog
from mainwindow import MainWindow
import helper


if __name__ == "__main__":
    a = QApplication(sys.argv)
    helper.dbConnect()

    loginDialog = LoginDialog()

    isAuth = False
    result = -1
    while not isAuth:
        result = loginDialog.exec_()
        if result == LoginDialog.Success or result == LoginDialog.Rejected:
            isAuth = True
        else:
            isAuth = False


    if result == LoginDialog.Success:
        w = MainWindow()
        w.show()
        a.exec_()

    sys.exit(-1)