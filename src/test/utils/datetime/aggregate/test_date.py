import unittest

from src.utils.datetime.aggregate.date import mindtdiff, avgdtdiff, dategroupduration, frecencyindex
from src.test.AggregateBaseUnitTestClass import AggregateBaseUnitTestClass


def generateMindTdiffDateTimeData():
    return ['2007-01-01 00:03:13'
        , '2007-01-01 00:03:27'
        , '2007-01-01 00:03:36'
        , '2007-01-01 00:04:39'
        , '2007-01-01 00:04:40'
        , '2007-01-01 00:04:49']


def generateDateGroupDurationDateTimeData():
    return ['2007-01-01 00:04:37'
        , '2007-01-01 00:04:39'
        , '2007-01-01 00:04:40'
        , '2007-01-01 00:04:49']


def generateFrecencyIndexDateTimeData():
    return ['2011-04-01 00:04:37'
        , '2011-01-01 00:04:39'
        , '2011-02-12 00:04:40'
        , '2011-02-14 00:04:49']


def generateDateData():
    return ['2007-01-01']


def generateNumericData():
    return ['2007']


def generateAvgTdiffDateTimeData():
    return ['2007-01-01 00:04:37'
        , '2007-01-01 00:04:39'
        , '2007-01-01 00:04:40'
        , '2007-01-01 00:04:49']


class TestMindTdiff(AggregateBaseUnitTestClass):

    def test_mindTdiff_dateTimeDate(self):
        mindTdiff = mindtdiff()
        dummyData = (x for x in generateMindTdiffDateTimeData())
        self.assertEqual(self.execute(mindTdiff, *dummyData), 1000)

    def test_mindTdiff_NoneData(self):
        mindTdiff = mindtdiff()
        dummyData = (x for x in generateDateData())
        self.assertEqual(self.execute(mindTdiff, *dummyData), None)

    def test_mindTdiff_NumericData(self):
        mindTdiff = mindtdiff()
        dummyData = (x for x in generateNumericData())
        self.assertEqual(self.execute(mindTdiff, *dummyData), None)

    def test_mindTdiff_NoArgs(self):
        mindTdiff = mindtdiff()
        self.assertEqual(self.execute(mindTdiff), None)


class TestAvgdTdiff(AggregateBaseUnitTestClass):

    def test_avgdtdiff_dateTimeDate(self):
        avgdTdiff = avgdtdiff()
        dummyData = (x for x in generateAvgTdiffDateTimeData())
        self.assertEqual(self.execute(avgdTdiff, *dummyData), 3000)

    def test_avgdtdiff_NoneData(self):
        avgdTdiff = avgdtdiff()
        dummyData = (x for x in generateDateData())
        self.assertEqual(self.execute(avgdTdiff, *dummyData), None)

    def test_avgdtdiff_NumericData(self):
        avgdTdiff = avgdtdiff()
        dummyData = (x for x in generateNumericData())
        self.assertEqual(self.execute(avgdTdiff, *dummyData), None)

    def test_avgdtdiff_NoArgs(self):
        avgdTdiff = avgdtdiff()
        self.assertEqual(self.execute(avgdTdiff), None)


class TestDateGroupDuration(AggregateBaseUnitTestClass):

    def test_dategroupduration_dateTimeDate(self):
        dateGroupDuration = dategroupduration()
        dummyData = (x for x in generateDateGroupDurationDateTimeData())
        self.assertEqual(self.execute(dateGroupDuration, *dummyData), 12)

    def test_dategroupduration_dateData(self):
        dateGroupDuration = dategroupduration()
        dummyData = (x for x in generateDateData())
        self.assertEqual(self.execute(dateGroupDuration, *dummyData), 0)


class TestFrecencyIndex(AggregateBaseUnitTestClass):

    def test_dategroupduration_dateTimeDate(self):
        frecencyIndex = frecencyindex()
        dummyData = (x for x in generateFrecencyIndexDateTimeData())
        self.assertEqual(0, self.execute(frecencyIndex, *dummyData))


if __name__ == '__main__':
    unittest.main()
