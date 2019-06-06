import unittest

from src.utils.text.aggregate.text import *
from src.test.AggregateBaseUnitTestClass import AggregateBaseUnitTestClass


def generateConcatGroupData():
    return ['word1 word2', ['word3', 'word4']]


class TestMindTdiff(AggregateBaseUnitTestClass):

    def test_mindTdiff_dateTimeDate(self):
        concatGroup = concatgroup()
        dummyData = (x for x in generateConcatGroupData())
        concatGroup.__init__()
        for arg in dummyData:
            concatGroup.step(*arg)
        for i in concatGroup.final():
            print(i)
        # for i in self.execute(concatGroup, *dummyData):
        #     print(i)



if __name__ == '__main__':
    unittest.main()
