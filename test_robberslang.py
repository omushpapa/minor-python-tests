import unittest
import robbers_language

class  Test_robberslangTestCase(unittest.TestCase):
    """Test robbers_language"""
    
    def test_returns_false_if_input_less_than_one(self):
        """Test returns false if input is less than one"""
        
        self.assertEqual(robbers_language.rob_string(""), False)
        
    def test_returns_false_if_input_not_string(self):
        """Test returns false is the input is not a string"""
        
        self.assertEqual(robbers_language.rob_string(1), False)
        
    def test_returns_false_if_digit_in_input(self):
        """Test returns false if the input has a digit"""
        
        self.assertEqual(robbers_language.rob_string("hell9"), False)
        
    def test_robs_string(self):
        """Test returns input in robbers language"""
        
        self.assertEqual(robbers_language.rob_string("this is fun"), "tothohisos isos fofunon")

if __name__ == '__main__':
    unittest.main()

