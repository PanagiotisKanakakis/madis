import unittest

from src.utils.datetime.row.tzconverter import *


def generateDateTimeData():
    return ['2010-12-05T00:00:00+00:00'
        , '2010-12-05T00:01:00+00:00'
        , '2010-12-05T00:02:00+00:00']


class TestTzConverter(unittest.TestCase):

    def test_tzconverter(self):
        rs = []
        expectedRs = ['2010-12-04T23:00:00-01:00', '2010-12-04T23:01:00-01:00', '2010-12-04T23:02:00-01:00']
        for arg in (x for x in generateDateTimeData()):
            rs.append(tzconverter(arg, '-01:00'))
        self.assertEqual(expectedRs, rs)


if __name__ == '__main__':
    unittest.main()
