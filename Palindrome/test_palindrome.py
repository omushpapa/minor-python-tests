import unittest
import palindrome

class  Test_palindromeTestCase(unittest.TestCase):
    """Tests palindrome"""
    
    def test_is_palindrome(self):
        """Test returns true if input is palindrome"""
        
        self.assertEqual(palindrome.reverse('radar'), True)
        self.assertEqual(palindrome.reverse('anna'), True)
        
    def test_is_not_palindrome(self):
        """Test returns false if input is not palindrome"""
        
        self.assertEqual(palindrome.reverse('radio'), False)
        self.assertEqual(palindrome.reverse('annete'), False)

if __name__ == '__main__':
    unittest.main()

