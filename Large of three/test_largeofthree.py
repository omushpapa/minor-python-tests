# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
import large_ofThree

class  Test_largeofthreeTestCase(unittest.TestCase):
    def test_returns_false_if_values_not_int(self):
        self.assertEqual(large_ofThree.max_of_three("p", "hi", "jngh"), False)
        self.assertEqual(large_ofThree.max_of_three("p", "hi", 6), False)
        self.assertEqual(large_ofThree.max_of_three(5, 2.3, "jngh"), False)
        
    def test_returns_largest_value(self):
        self.assertEqual(large_ofThree.max_of_three(3, 5, 9), 9)
        self.assertEqual(large_ofThree.max_of_three(3, 3, 8), 8)
        self.assertEqual(large_ofThree.max_of_three(3, 7, 7), 7)
        
    def test_returns_equal_if_values_same(self):
        self.assertEqual(large_ofThree.max_of_three(66, 66, 66), 66)

if __name__ == '__main__':
    unittest.main()

