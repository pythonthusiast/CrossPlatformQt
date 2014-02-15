import unittest
from PyQt4.QtCore import QCoreApplication
from auth import Auth
import helper
import sys

class TestCase01(unittest.TestCase):
    def testConnect(self):
        qApp = QCoreApplication(sys.argv)
        self.assertTrue(helper.dbConnect())

    def testMd5(self):
        self.assertEqual(helper.computeHash("password"),"5f4dcc3b5aa765d61d8327deb882cf99")

    def testAuth(self):
        qApp = QCoreApplication(sys.argv)
        helper.dbConnect()
        auth = Auth()
        self.assertEqual(auth.doLogin("eko", "password"), True)

if __name__ == "__main__":
    unittest.main()