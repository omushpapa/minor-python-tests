import unittest
import membership

class  Test_membershipTestCase(unittest.TestCase):
    """Tests membership"""
    
    def setUp(self):
        """Set up initial list"""
        
        self.int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.string_list = ['yes', 'injection', 'introduce', 'hello', 'y', '9', '0']
        
    def test_int_value_int_list(self):
        """Test for int value in int list, return True is found False otherwise"""
        
        self.assertEqual(membership.is_member(2, self.int_list), True)
        self.assertEqual(membership.is_member(99, self.int_list), False)
        
    def test_int_value_string_list(self):
        """Test returns True if int value found in string list, False otherwise"""
        
        self.assertEqual(membership.is_member(2, self.string_list), False)
        self.assertEqual(membership.is_member(9, self.string_list), True)
        
    def test_string_value_string_list(self):
        """Test returns True if string value found in string list, False otherwise"""
        
        self.assertEqual(membership.is_member('hello', self.string_list), True)
        self.assertEqual(membership.is_member('9', self.string_list), True)
        self.assertEqual(membership.is_member('dictionary', self.string_list), False)
        
    def test_string_value_int_list(self):
        """Test returns True if string value found in int list, False otherwise"""
        
        self.assertEqual(membership.is_member('hi', self.int_list), False)
        self.assertEqual(membership.is_member('8', self.int_list), True)

if __name__ == '__main__':
    unittest.main()