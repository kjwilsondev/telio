#!python

from set import Set
import unittest


class SetTest(unittest.TestCase):

    def test_init(self):
        s = Set()
        assert s.size == 0
    
    def test_contains(self):
        s = Set(4, ['a', 'b', 'c'])
        assert s.contains('b') is True
        assert s.contains('d') is False
        assert s.contains('c') is True

if __name__ == '__main__':
    unittest.main()