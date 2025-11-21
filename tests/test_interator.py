import types
import unittest

from FlatIterator import FlatIterator
from main import flat_generator

class TestMain(unittest.TestCase):
    
    def setUp(self):
        self.list_of_lists_1 = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f', 'h', False],
            [1, 2, None]
        ]
        self.list_of_lists_2 = [
            [['a'], ['b', 'c']],
            ['d', 'e', [['f'], 'h'], False],
            [1, 2, None, [[[[['!']]]]], []]
        ]
        
        self.true_list = ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
        self.true_list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
        
    def tearDown(self):
        del self.list_of_lists_1
        del self.true_list
        del self.list_of_lists_2
    
    def test_iterator(self):
        flatiterator = FlatIterator(self.list_of_lists_1)
        for flat_iterator_item, check_item in zip(flatiterator, self.true_list): 
            self.assertEqual(flat_iterator_item, check_item)
            
        self.assertListEqual(list(flatiterator), self.true_list)
        
    def test_flat_generator(self):
        for flat_iterator_item, check_item in zip(flat_generator(self.list_of_lists_1), self.true_list): 
            self.assertEqual(flat_iterator_item, check_item)
            
        self.assertListEqual(list(flat_generator(self.list_of_lists_1)), self.true_list)
        self.assertIsInstance(flat_generator(self.list_of_lists_1), types.GeneratorType)
        
    def test_iterator_with_nested_list(self):
        flatiterator_nested = FlatIterator(self.list_of_lists_2)
        for flat_iterator_item, check_item in zip(flatiterator_nested, self.true_list2): 
            self.assertEqual(flat_iterator_item, check_item)
            
        self.assertListEqual(list(flatiterator_nested), self.true_list2)

    def test_flat_generator_with_nested_list(self):
        for flat_iterator_item, check_item in zip(flat_generator(self.list_of_lists_2), self.true_list2): 
            self.assertEqual(flat_iterator_item, check_item)
            
        self.assertListEqual(list(flat_generator(self.list_of_lists_2)), self.true_list2)
        self.assertIsInstance(flat_generator(self.list_of_lists_2), types.GeneratorType)