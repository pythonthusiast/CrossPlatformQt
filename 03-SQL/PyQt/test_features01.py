import unittest
from auth import Auth

class TestCase01(unittest.TestCase):
    def testAuth(self):
        auth = Auth()
        self.assertEqual(auth.doLogin("eko", "oke"), True)
        
    def testError(self, ):
        self.assertEqual(5,10);
    

if __name__ == "__main__":
    unittest.main()

