import unittest

import solution


class TestNarcissistic(unittest.TestCase):

    def test_is_narcissistic(self):
        self.assertFalse(solution.is_narcissistic('10'))

        self.assertTrue(solution.is_narcissistic('223', 4))

        self.assertTrue(solution.is_narcissistic('0'))

        self.assertTrue(solution.is_narcissistic('1'))

        self.assertTrue(solution.is_narcissistic('54748'))

        self.assertTrue(solution.is_narcissistic('5A07C', 16))

        self.assertTrue(solution.is_narcissistic('13579', 16))

if __name__ == '__main__':
    unittest.main()

