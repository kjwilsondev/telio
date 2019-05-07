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
    
    def test_add(self):
        s = Set(4, ['a', 'b', 'c'])
        assert s.size is 3
        s.add('dont fail me!')
        assert s.size is 4
        s.add('im working hard to write tests!')
        assert s.size is 5
        s.add('ill finish tonight!')
        assert s.size is 6

    def test_remove(self):
        s = Set(4, ['a', 'b', 'c'])
        assert s.size is 3
        s.remove('a')
        assert s.size is 2
        s.remove('b')
        assert s.size is 1
        s.remove('c')
        assert s.size is 0
    
    def test_union(self):
        s = Set(4, ['yes', 'no', 'maybe'])
        t = Set(4, ['yea', 'na', 'maybe'])
        assert s.union(t).contains('maybe')

if __name__ == '__main__':
    unittest.main()