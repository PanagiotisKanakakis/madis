import unittest

from src.utils.files.vtable.dirfiles import dirfiles
from src.functions.vtable.vtbase import *


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


def generateDate2IsoData():
    return ['2007-12-31'
        , '2010-01-01'
        , '2010W06'
        , '"18/Jan/2011:11:13:00 +0100"']


class TestDirFiles(unittest.TestCase):

    def test_dirfiles(self):
        rs = []
        expectedRs = ['2009-01-01 01:03:13', '2009-01-01 01:03:13', '2009-01-01 01:03:13', '2009-01-01 01:03:13',
                      '2009-01-01 01:03:13', '2009-01-01 01:03:13']
        # for arg in (x for x in generateCleanTimezoneDateTimeData()):
        #     rs.append(cleantimezone(arg))
        # self.assertEqual(expectedRs, rs)
        f = dirfiles()
        for x in f.VTiter(str('.')):
            print(x)


if __name__ == '__main__':
    unittest.main()
