import unittest
import operate_list

class  Test_listoperateTestCase(unittest.TestCase):
    """Tests operate_list"""
    
    def test_num_input(self):
        """Test returns result"""
        self.assertEqual(operate_list.sum([2, 4, 6]), 12)
        self.assertEqual(operate_list.multiply([2, 4, 6]), 48)
        
    def test_string_input(self):
        """Test returns false if input is string"""
        
        self.assertEqual(operate_list.sum(['ferg', 2, 3]), False)
        self.assertEqual(operate_list.multiply(['ferg', 2, 3]), False)
        
    def test_no_input(self):
        """Test returns false if input is empty"""
        
        self.assertEqual(operate_list.sum(""), False)
        self.assertEqual(operate_list.sum([]), False)
        self.assertEqual(operate_list.multiply([]), False)
        self.assertEqual(operate_list.multiply([]), False)
        
    def test_when_none(self):
        """Test returns false if input is empty"""
        
        self.assertEqual(operate_list.sum(None), False)
        self.assertEqual(operate_list.multiply(None), False)


if __name__ == '__main__':
    unittest.main()

