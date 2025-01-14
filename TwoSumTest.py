import unittest
from TwoSum import twoSum


class MyTestCase(unittest.TestCase):
    def TwoSumTest(self):
        self.assertEqual(twoSum([2, 7, 11, 15], 9), 1)  # add assertion here


if __name__ == '__main__':
    unittest.main()
