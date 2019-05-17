import unittest

from src.utils.network.row.htmlops import *


def generateUrlSplitData():
    return ['http://www.test.com/apath/bpath/fname.pdf', 'http://www.test.com/search.csv;p=5?q=test#hl=en']


class TestHtmlOps(unittest.TestCase):

    def test_urlsplit(self):
        rs = []
        expectedRs = []
        for arg in (x for x in generateUrlSplitData()):
            rs.append(urlsplit(arg))
        for x in rs:
            for y in x:
                print(y)


if __name__ == '__main__':
    unittest.main()
