import unittest
import largest

class  Test_largestTestCase(unittest.TestCase):
    def test_string_list(self):
        self.assertEqual(largest.max_in_list(['lk', 'j', 9]), False)
        
    def test_int_list(self):
        self.assertEqual(largest.max_in_list([600,400,800,990]), 990)
        self.assertEqual(largest.max_in_list([580,600,400,590]), 600)
        
    def test_single_value(self):
        self.assertEqual(largest.max_in_list(6), 6)
        self.assertEqual(largest.max_in_list([6]), 6)

if __name__ == '__main__':
    unittest.main()