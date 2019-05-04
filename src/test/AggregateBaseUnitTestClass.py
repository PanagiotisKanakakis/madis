import unittest


class AggregateBaseUnitTestClass(unittest.TestCase):

    def setUp(self):
        pass

    def execute(self, udf, *args):
        for arg in args:
            udf.step(arg)
        return udf.final()
