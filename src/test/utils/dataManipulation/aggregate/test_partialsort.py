import unittest

from src.utils.dataManipulation.aggregate.partialsort import *
from src.test.AggregateBaseUnitTestClass import AggregateBaseUnitTestClass


def generatePartialSortData():
    return [(3, 'a', 'b', ['aa', '43']),
            (3, 'a', 'b', ['ac', '34']),
            (3, 'a', 'b', ['ab', '21']),
            (3, 'a', 'b', ['as', '23'])]


result = [('aa', '43'),
          'ab ,21',
          'ac  ,34',
          'as  ,23']


class TestPartialSort(AggregateBaseUnitTestClass):

    def test_partialSort(self):
        partialSort = partialsort()
        # dummyData = (x for x in generatePartialSortData())
        # self.assertEqual(self.execute(partialSort, *dummyData), 3)

        dummyData = (x for x in generatePartialSortData())
        partialSort.__init__()
        for arg in dummyData:
            partialSort.step(*arg)
        for i in partialSort.final():
            print(i)
        # self.assertEqual(partialSort.final(), result)


if __name__ == '__main__':
    unittest.main()
