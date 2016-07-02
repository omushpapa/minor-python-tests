import unittest
import longest

class  Test_longestTestCase(unittest.TestCase):
    def test_string_list(self):
        self.assertListEqual(
            ['longest', 'strong', 'y', False],
            [
                longest.find_longest_word(['yet', 'peep', 'longest', 'j']),
                longest.find_longest_word(['ye', 'strong', 'hw', '1']),
                longest.find_longest_word(['', 'y', '', '']),
                longest.find_longest_word(['', '', '', ''])
            ]
        )
        
    def test_int_list(self):
        self.assertListEqual(
            [False, '7'],
            [
                longest.find_longest_word([7, 6, 5, 4]),
                longest.find_longest_word([4, 5, '7', 8])
            ]
        )
        
    def test_empty_list(self):
        self.assertEqual(False, longest.find_longest_word([]))
        
if __name__ == '__main__':
    unittest.main()