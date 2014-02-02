import sys
from PyQt5.Qt import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel("Hello Qt!")
    label.show()
    app.exec()