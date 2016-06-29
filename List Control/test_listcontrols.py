import unittest
import list_controls

class  Test_listcontrolsTestCase(unittest.TestCase):
    """Tests list_controls"""
    
    def test_returns_false_if_not_list(self):
        """Test returns false if input is not a list"""
        
        self.assertEqual(list_controls.sum(1), False)
        self.assertEqual(list_controls.multiply(1), False)
        
    def test_returns_false_if_list_has_string(self):
        """Test returns false if the list has a string or character value"""
        
        self.assertEqual(list_controls.sum([7, 'yu']), False)
        self.assertEqual(list_controls.multiply([7, 'yu']), False)
        
    def test_returns_sum_of_values(self):
        """Test returns the sum of the values in the list"""
        
        self.assertEqual(list_controls.sum([4, 5, 2]), 11)
        
    def test_returns_result_of_multiplication(self):
        """Test returns the result of the multiplication of the list value"""
        
        self.assertEqual(list_controls.multiply([4, 5, 2]), 40)

if __name__ == '__main__':
    unittest.main()

