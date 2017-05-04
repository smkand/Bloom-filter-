import unittest

from bloomfil import BloomFilter


class Mytest(unittest.TestCase):

    # preparing to test
    def setUp(self):
        self.bloomfil = BloomFilter(1024000, 5)
        self.bloomfil.add("semantic")

    def test_lookup(self):
        self.assertEquals(self.bloomfil.lookup("semantic"), "Probably")

if __name__ == '__main__':
    unittest.main()
