# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
import string_length

class  Test_stringlengthTestCase(unittest.TestCase):
    def test_return_false_if_string_empty(self):
        self.assertEqual(string_length.string_length(None), False)
    
    def test_value_is_int(self):
        self.assertEqual(string_length.string_length(7), False)
        
    def test_value_is_bool(self):
        self.assertEqual(string_length.string_length(True), False)
        
    def test_returns_length_of_value(self):
        self.assertEqual(string_length.string_length("hello"), 5)
    
    def test_returns_length_of_list(self):
        self.assertEqual(string_length.string_length(["fe","hsa", 6]), 3)
        self.assertEqual(string_length.string_length(["fe","hsa", 6, 6.9]), 4)

if __name__ == '__main__':
    unittest.main()

