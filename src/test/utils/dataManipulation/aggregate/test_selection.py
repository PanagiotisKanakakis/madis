import unittest

from src.utils.dataManipulation.aggregate.selection import *
from src.test.AggregateBaseUnitTestClass import AggregateBaseUnitTestClass


def generateImaxData():
    return [(3, [34, 'la']),
            (3, [18, 'lo']),
            (3, [120.0, 'all'])]


def generateMinRowData():
    return [[34, 'la'],
            [18, 'lo'],
            [120.0, 'all']]


def generateGroupDiffData():
    return [[0, 'a'],
            [0, 'b'],
            [1, 'c'],
            [1, 'd'],
            [2, 'e'],
            [3, 'e'],
            [3, 'f'],
            [3, 'g']]


def generateOnTopData():
    return [(2, 'a', 'b', [34, 'la']),
            (2, 'a', 'b', [18, 'lo']),
            (2, 'a', 'b', [120.0, 'all'])]


class TestSelection(AggregateBaseUnitTestClass):

    def test_imax(self):
        iMax = imax()
        dummyData = (x for x in generateImaxData())
        iMax.__init__()
        for arg in dummyData:
            iMax.step(*arg)
        self.assertEqual(iMax.final(), [18, 'lo'])

    def test_minrow(self):
        minRow = minrow()
        dummyData = (x for x in generateMinRowData())
        minRow.__init__()
        for arg in dummyData:
            minRow.step(*arg)
        self.assertEqual(minRow.final(), 'lo')

    def test_maxrow(self):
        maxRow = maxrow()
        dummyData = (x for x in generateMinRowData())
        maxRow.__init__()
        for arg in dummyData:
            maxRow.step(*arg)
        self.assertEqual(maxRow.final(), 'all')

    def test_groupdiff(self):
        groupDiff = groupdiff()
        dummyData = (x for x in generateGroupDiffData())
        groupDiff.__init__()
        for arg in dummyData:
            groupDiff.step(*arg)
        for i in groupDiff.final():
            print(i)

    def test_ontop(self):
        onTop = ontop()
        dummyData = (x for x in generateOnTopData())
        onTop.__init__()
        for arg in dummyData:
            onTop.step(*arg)
        for i in onTop.final():
            print(i)


if __name__ == '__main__':
    unittest.main()
