import unittest

from src.utils.files.vtable.file import *


class TestDirFiles(unittest.TestCase):

    def test_file(self):
        f = FileVT()
        args = (x for x in 'http://sites.google.com/site/stats202/data/test_data.csv?attredirects=0')
        for x in f.open():
            print(x)


if __name__ == '__main__':
    unittest.main()
