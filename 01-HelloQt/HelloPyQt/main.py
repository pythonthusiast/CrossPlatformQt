import sys
from PyQt4.Qt import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel("Hello Qt!")
    label.show()
    app.exec_()