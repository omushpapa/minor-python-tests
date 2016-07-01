import unittest
import maps

class  Test_mapTestCase(unittest.TestCase):
    """Tests maps"""
    
    def test_string_list(self):
        """Test returns the length of string elements in each
           list
        """
        
        self.assertListEqual(
            [
                [5, 3, 1],
                [3, 5],
                [20, 13, 0]
            ],
            [
                maps.map_list(['hello', 'why', 'y']),
                maps.map_list(['yes', 'enjoy']),
                maps.map_list(['15236487921068952470', 'commemoration', ''])
            ])
                            
    def test_int_list(self):
        """Test returns False if input is list of integers"""
        
        self.assertEqual(False, 
            maps.map_list([1, 2, 3]))
            
    def test_tuple_input(self):
        """Test returns False if input is tuple"""
        
        self._tuple1 = 1, 2, 3
        self._tuple2 = 'yes', 'y', 'hey'
        self.assertEqual(False, maps.map_list(self._tuple1))
        self.assertEqual(False, maps.map_list(self._tuple2))
        
    def test_string_input(self):
        """Test returns False if input is string or int"""
        
        self.assertEqual(False, maps.map_list(1))
        self.assertEqual(False, maps.map_list('false'))

if __name__ == '__main__':
    unittest.main()