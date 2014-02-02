import sys
from PySide.QtGui import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel("Hello Qt!")
    label.show()
    app.exec_()