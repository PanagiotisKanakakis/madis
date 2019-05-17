import unittest

from src.utils.shell.vtable.jsonpipe import *


class TestJsonPipe(unittest.TestCase):

    def test_jsonpipe(self):
        f = JSONPipeVT()
        for x in f.VTiter(str('wc test_pipe.py')):
            print(x)


if __name__ == '__main__':
    unittest.main()
