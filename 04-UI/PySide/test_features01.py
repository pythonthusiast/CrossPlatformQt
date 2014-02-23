import unittest
from PySide.QtCore import QCoreApplication
from auth import Auth
import helper
import sys

class TestCase01(unittest.TestCase):
    def testConnect(self):

        self.assertTrue(helper.dbConnect())

    def testMd5(self):
        self.assertEqual(helper.computeHash(str("password")),"5f4dcc3b5aa765d61d8327deb882cf99")

    def testAuth(self):
        helper.dbConnect()
        auth = Auth()
        self.assertEqual(auth.doLogin("eko", "password"), True)

if __name__ == "__main__":
    unittest.main()