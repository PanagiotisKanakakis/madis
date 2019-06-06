import unittest

from src.utils.dataManipulation.aggregate.subgroup import *
from src.test.AggregateBaseUnitTestClass import AggregateBaseUnitTestClass


def generateGroupSumData():
    return [[1, ('aa', 't1', 43)],
            ['ac', 't2', 34],
            ['aa', 't3', 12]]
    # (1, 'a', ['ab', 't4', 21]),
    # (1, 'a', ['ac', 't5', 14]),
    # (1, 'a', ['as', 't6', 23])]


class TestSubgroup(AggregateBaseUnitTestClass):

    def test_groupsum(self):
        groupSum = groupsum()

        dummyData = (x for x in generateGroupSumData())
        groupSum.__init__()
        groupSum.notchecked = False
        groupSum.grouplen = 1
        groupSum.numofargs = 3
        for arg in dummyData:
            groupSum.step(*arg)
        for i in groupSum.final():
            print(i)
        # self.assertEqual(partialSort.final(), result)


if __name__ == '__main__':
    unittest.main()
