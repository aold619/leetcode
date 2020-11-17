import unittest
from leetcode.two_sum import Solution


CASE_1 = [2, 3, 5, 9, 8, 11]
CASE_2 = [3, 2, 4]
CASE_3 = [3, 3]


class TestTwoSum(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_two_sum(self):
        self.assertEqual([0, 1], Solution().two_sum(CASE_1, 5))
        self.assertEqual([], Solution().two_sum(CASE_1, 23))
        self.assertEqual([], Solution().two_sum([], 5))

        self.assertEqual([1, 2], Solution().two_sum(CASE_2, 6))
        self.assertEqual([0, 1], Solution().two_sum(CASE_3, 6))


if __name__ == '__main__':
    unittest.main()
