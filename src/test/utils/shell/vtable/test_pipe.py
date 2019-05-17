import unittest

from src.utils.shell.vtable.pipe import *


class TestPipe(unittest.TestCase):

    def test_pipe(self):
        f = PipeVT()
        for x in f.VTiter(str('wc test_pipe.py')):
            print(x)


if __name__ == '__main__':
    unittest.main()
