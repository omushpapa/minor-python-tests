import unittest
import generator

class  Test_generatorTestCase(unittest.TestCase):
    """Tests generator"""
    
    def test_negative_reps(self):
        """Test returns False if repetitions is negative"""
        
        self.assertEqual(generator.generate_n_chars(-2, 'f'), False)
        
    def test_many_chars(self):
        """Test returns False if input is more than one character"""
        
        self.assertEqual(generator.generate_n_chars(3, '0.6'), False)
        
    def test_reps_is_positive(self):
        """Test returns number of chars"""
        
        self.assertEqual(generator.generate_n_chars(15, 'h'), 'hhhhhhhhhhhhhhh')
        
    def test_string_is_num(self):
        """Test returns number of chars if input is digit"""
        
        self.assertEqual(generator.generate_n_chars(6, '1'), '111111')

if __name__ == '__main__':
    unittest.main()

