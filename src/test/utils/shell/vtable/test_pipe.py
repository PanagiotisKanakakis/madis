import unittest

from src.utils.shell.vtable.pipe import *


class TestPipe(unittest.TestCase):

    def test_pipe_wc(self):
        f = PipeVT()
        for x in f.VTiter(str('wc test_pipe.py')):
            print(x)

    def test_pipe_ls(self):
        f = PipeVT()
        for x in f.VTiter(str('ls -lha .')):
            print(x)


if __name__ == '__main__':
    unittest.main()
