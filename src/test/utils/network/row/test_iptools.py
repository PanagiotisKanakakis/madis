import unittest

from src.utils.network.row.iptools import *


def generateUrlSplitData():
    return ['123.123.123.123']


def generateColumnSeparatedData():
    return ['123,123,123,123']


class TestHtmlOps(unittest.TestCase):

    def test_urlsplit(self):
        rs = []
        expectedRs = [2071690107]
        for arg in (x for x in generateUrlSplitData()):
            rs.append(ip2long(arg))
        self.assertEqual(expectedRs, rs)

    def test_urlsplitColumn(self):
        rs = []
        expectedRs = [2071690107]
        for arg in (x for x in generateColumnSeparatedData()):
            rs.append(ip2long(arg))
        self.assertEqual(expectedRs, rs)


if __name__ == '__main__':
    unittest.main()
