import unittest
from unittest.mock import patch

from src.utils.dataManipulation.vtable.sample import *


def input():
    return 'query:select * from (James, 10, 2)'


class TestSample(unittest.TestCase):

    # @patch("src.functions.Connection.cursor", return_value=[('James', 10, 2)])
    def test_sample(self):
        with patch('src.functions.Connection') as mocksql:
            mocksql.cursor().execute().return_value = [('James', 10, 2)]
            f = SampleVT()
            for x in f.VTiter(input()):
                print(x)


if __name__ == '__main__':
    unittest.main()
