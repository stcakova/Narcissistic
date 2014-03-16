import unittest

import solution


class TestNarcissistic(unittest.TestCase):

    def test_is_narcissistic(self):
        
        self.assertFalse(solution.is_narcissistic('10'))

        self.assertTrue(solution.is_narcissistic('223', 4))

        self.assertTrue(solution.is_narcissistic('0'))

        self.assertTrue(solution.is_narcissistic('1'))
        
        self.assertFalse(solution.is_narcissistic('C00C9', 16))

        self.assertTrue(solution.is_narcissistic('54748'))

        self.assertTrue(solution.is_narcissistic('5A07C', 16))

        self.assertTrue(solution.is_narcissistic('13579', 16))

        self.assertTrue(solution.is_narcissistic('124030', 5))

        self.assertTrue(solution.is_narcissistic('570', 9))

        self.assertFalse(solution.is_narcissistic('103'))

        self.assertTrue(solution.is_narcissistic('122', 3))
        
        self.assertTrue(solution.is_narcissistic('570', 9))
        
        self.assertTrue(solution.is_narcissistic('5A47C', 16))
        
        self.assertTrue(solution.is_narcissistic('12205', 7))
        
       

if __name__ == '__main__':
    unittest.main()
