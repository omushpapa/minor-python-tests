# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
import overlap

class  Test_overlapTestCase(unittest.TestCase):
    """Tests overlap"""
    
    def setUp(self):
        """Initialises lists"""
        
        self.int_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.string_list = ['0', 'h', 'hello', 'dictionary', 'frequency', 'avail']
        self.mixed_list = [2, 4, 'yes', 'y']
        
    def test_int_list(self):
        """Test returns True if common element found between int and string list"""
        
        self.assertEqual(overlap.overlapping(self.int_list, self.string_list), True)
        
    def test_string_list(self):
        """Test returns True if common element found between string and int list"""
        
        self.assertEqual(overlap.overlapping(self.string_list, self.int_list), True)
        
    def test_mixed_list(self):
        """Test returns True if common element found between lists False otherwise"""
        
        self.assertEqual(overlap.overlapping(self.mixed_list, self.string_list), False)
        self.assertEqual(overlap.overlapping(self.mixed_list, self.int_list), True)

if __name__ == '__main__':
    unittest.main()

