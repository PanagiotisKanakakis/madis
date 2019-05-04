import unittest

from src.utils.datetime.row.date import *


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


class TestDate(unittest.TestCase):

    def test_cleantimezone(self):
        rs = []
        expectedRs = ['2009-01-01 01:03:13', '2009-01-01 01:03:13', '2009-01-01 01:03:13', '2009-01-01 01:03:13',
                      '2009-01-01 01:03:13', '2009-01-01 01:03:13']
        for arg in (x for x in generateCleanTimezoneDateTimeData()):
            rs.append(cleantimezone(arg))
        self.assertEqual(expectedRs, rs)

    def test_activityindex(self):
        rs = []
        expectedRs = [0, 0, 0, 0]
        for arg in (x for x in generateActivityIndexDateTimeData()):
            rs.append(activityindex(arg))
        self.assertEqual(expectedRs, rs)

    def test_sectohuman(self):
        rs = []
        expectedRs = ['3 sec'
            , '1 min 3 sec'
            , '2 hours 46 min 40 sec'
            , '1 day 3 hours 46 min 40 sec'
            , '11 days 13 hours 46 min 40 sec']
        for arg in (x for x in generateSecToHumanData()):
            rs.append(sectohuman(arg))
        self.assertEqual(expectedRs, rs)

    def test_date2iso(self):
        rs = []
        expectedRs = ['2007-12-31T00:00:00'
                     , '2010-01-01T00:00:00'
        , '2010-02-05T00:00:00'
        , '2011-01-18T11:13:00+01:00']
        for arg in (x for x in generateDate2IsoData()):
            rs.append(date2iso(arg))
        self.assertEqual(expectedRs, rs)


if __name__ == '__main__':
    unittest.main()
