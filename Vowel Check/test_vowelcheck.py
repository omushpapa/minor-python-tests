import unittest
import vowel_check

class  Test_vowelcheckTestCase(unittest.TestCase):
    """Test vowel_check"""
    
    def test_returns_false_if_input_is_string(self):
        """Test returns false if the input is a string"""
        
        self.assertEqual(vowel_check.is_vowel("ghi"), False)
        
    def test_return_false_if_input_less_than_zero(self):
        """Test returns false if no input or input is less than zero"""
        
        self.assertEqual(vowel_check.is_vowel(-1), False)
        self.assertEqual(vowel_check.is_vowel(0.9), False)
        
    def test_returns_true_for_vowel(self):
        """Test returns true if input is a vowel"""
        
        self.assertEqual(vowel_check.is_vowel('i'), True)
        
    def test_returns_false_for_other(self):
        """Test returns false if input is alphanumeric but not a vowel"""
        
        self.assertEqual(vowel_check.is_vowel('!'), False)
        self.assertEqual(vowel_check.is_vowel('h'), False)

if __name__ == '__main__':
    unittest.main()