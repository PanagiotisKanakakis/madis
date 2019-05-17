import unittest

from src.utils.files.vtable.dirfiles import dirfiles


class TestDirFiles(unittest.TestCase):

    def test_dirfiles(self):
        f = dirfiles()
        for x in f.VTiter(str('.')):
            print(x)

    def test_dirfiles_rec(self):
        f = dirfiles()
        args = (x for x in ('rec:1', '../../datetime'))
        for x in f.VTiter(*args):
            print(x)


if __name__ == '__main__':
    unittest.main()
