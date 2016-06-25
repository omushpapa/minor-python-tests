# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
import large_num

class  Test_largenumTestCase(unittest.TestCase):
    def test_returns_false_if_values_not_int(self):
        self.assertEqual(large_num.max("py","px"), False)
    
    def test_returns_equal_if_equal(self):
        self.assertEqual(large_num.max(2,2), "Equal")
        
    def test_return_largest_num(self):
        self.assertEqual(large_num.max(2,3), 3)
        self.assertEqual(large_num.max(7,4), 7)

if __name__ == '__main__':
    unittest.main()

