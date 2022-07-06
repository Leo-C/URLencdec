import unittest
from URLencdec import URLencode, URLdecode


class Test_URLencoding(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_encode(self):
        dec = "\"Hello ;word9&"
        enc = URLencode(dec)
        self.assertEqual(enc, "%22Hello+%3Bword9%26");
    
    def test_decode(self):
        enc = "%22Hello+%3Bword9%26"
        dec = URLdecode(enc)
        self.assertEqual(dec, "\"Hello ;word9&");
        
        enc = "%22Hello%20%3Bword9%26"
        dec = URLdecode(enc)
        self.assertEqual(dec, "\"Hello ;word9&");
