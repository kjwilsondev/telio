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
        assert s.union(t).contains('yes') and s.union(t).contains('yea')
        s = Set(4, ['bro', 'bruh', 'brother'])
        t = Set(4, ['bud', 'buddy', 'browski'])
        assert s.union(t).contains('bro') and s.union(t).contains('browski')
        s = Set(4, ['yea', 'na', 'maybe'])
        t = Set(4, ['yea', 'na', 'maybe'])
        assert s.union(t).contains('yea')  and s.union(t).contains('na') and s.union(t).contains('maybe')

    def test_intersection(self):
        s = Set(4, ['yes', 'no', 'maybe'])
        t = Set(4, ['yea', 'na', 'maybe'])
        assert s.union(t).contains('maybe')
        s = Set(4, ['yea', 'no', 'maybe'])
        t = Set(4, ['yea', 'na', 'maybe'])
        assert s.union(t).contains('yea') and s.union(t).contains('maybe')
        s = Set(4, ['yea', 'na', 'maybe'])
        t = Set(4, ['yea', 'na', 'maybe'])
        assert s.union(t).contains('yea')  and s.union(t).contains('na') and s.union(t).contains('maybe')

    def test_difference(self):
        s = Set(4, ['yes', 'no', 'maybe'])
        t = Set(4, ['yea', 'na', 'maybe'])
        assert s.difference(t).contains('yes') and s.difference(t).contains('yea')
        assert s.difference(t).contains('maybe') is False
        s = Set(4, ['bro', 'bruh', 'brother'])
        t = Set(4, ['bud', 'buddy', 'browski'])
        assert s.difference(t).contains('bro') and s.difference(t).contains('bud')
        s = Set(4, ['bro', 'bruh', 'brother'])
        t = Set(4, ['bro', 'buddy', 'browski'])
        assert s.difference(t).contains('bruh') and s.difference(t).contains('browski')
        assert s.difference(t).contains('bro') is False

    def test_is_subset(self):
        s = Set(4, ['yes', 'no', 'maybe'])
        t = Set(4, ['yea', 'na', 'maybe'])
        assert s.is_subset(t) is False
        s = Set(4, ['yes', 'no', 'maybe'])
        t = Set(4, ['yes', 'no', 'maybe', 'finally'])
        assert s.is_subset(t) is True
        s = Set(4, ['yes', 'no', 'maybe'])
        t = Set(4, ['yes', 'no', 'maybe', 'finally'])
        assert t.is_subset(s) is False


if __name__ == '__main__':
    unittest.main()