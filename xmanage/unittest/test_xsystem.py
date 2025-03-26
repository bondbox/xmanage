# coding:utf-8

import unittest

from xmanage import xsystem


class TestSysPath(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_main(self):
        self.assertEqual(xsystem.main(["path"]), 0)


if __name__ == "__main__":
    unittest.main()
