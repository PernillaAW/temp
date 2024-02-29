
import unittest
from guess import test


class TestDiceClass(unittest.TestCase):

    def test_init_object(self):
        res = test.Test()
        self.assertIsInstance(res, test.Test)
