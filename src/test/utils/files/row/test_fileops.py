import unittest

from src.utils.files.row.fileops import *


def generateCleanTimezoneDateTimeData():
    return ['2009-01-01T01:03:13+0100'
        , '2009-01-01T01:03:13-0100'
        , '2009-01-01T01:03:13+01:00'
        , '2009-01-01T01:03:13-01:00'
        , '2009-01-01T01:03:13+01'
        , '2009-01-01T01:03:13-01']


def generateActivityIndexDateTimeData():
    return ['2009-01-01T01:32:03Z'
        , '2010-01-01T00:03:13Z'
        , '2010-12-31T00:03:13Z'
        , '2011-04-01T00:03:13Z']


def generateSecToHumanData():
    return ['3', '63', '10000'
        , ' 100000'
        , '1000000']


def generateFileExtensionData():
    return ['http://www.test.com/lalala.gif', 'http://www.test.com/lalala.GIF']


class TestFileOps(unittest.TestCase):

    def test_fileextension(self):
        rs = []
        expectedRs = ['.gif', '.gif']
        for arg in (x for x in generateFileExtensionData()):
            rs.append(fileextension(arg))
        self.assertEqual(expectedRs, rs)


if __name__ == '__main__':
    unittest.main()
