import unittest
import reverse

class  Test_reverseTestCase(unittest.TestCase):
    """Tests reverse"""
    
    def test_word(self):
        self.assertEqual(reverse.reverse('word'), 'drow')
        
    def test_characters(self):
        self.assertEqual(reverse.reverse('!1$t6'), '6t$1!')

if __name__ == '__main__':
    unittest.main()

