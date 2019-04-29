from hashset import HashSet
from linkedlist import LinkedList

class Set(HashSet):

    def __init__(self, init_size=8, elements=None):
        """Initializes the set with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]
        self.size = 0  # Number of key-value entries
        if elements is not None:
            for item in elements:
                self.set(item)
                self.size += 1

    def __contains__(self, element):
        """
        Returns a boolean indicating whether element is in set

        Running time: O(2n) => O(n)

        contains func: O(2n)
        - hash funciton in bucket index is O(n) where n is the width of a number
        - find function traverses through key values making it O(n)
        """
        return self.contains(element)

    def add(self, element):
        """
        Adds element to set
        If present already, returns None

        Running time: O(5n) => O(n)

        contains func: O(2n)
        - hash funciton in bucket index is O(n) where n is the width of a number
        - find function traverses through key values making it O(n)

        set func: O(3n)
        - hash funciton in bucket index is O(n) where n is the width of a number
        - find function traverses through items making it O(n)
        - if load factor > .75, the resize method creates a new linkedlist making it O(n)
        """
        if self.contains(element):
            return None
        self.set(element)
        self.size += 1

    def remove(self, element):
        """
        Removes element from this set if present
        or
        raises KeyError

        Running time: O(2n) => O(n)

        delete func: O(2n)
        - hash funciton in bucket index is O(n) where n is the width of a number
        - find function traverses through items making it O(n)
        """
        self.delete(element)
        self.size -= 1

    def union(self, other_set):
        """
        Returns new_set that is the union of this set and other_set

        Running time: O(4n + 4m) => O(n) or O(m)
        n = original set entries 
        m = other_set entries

        - traverses through each item in self making it O(n)
        - traverses through each item in other_set making it O(m)

        add func: O(3n + 3m)
        - hash funciton in bucket index is O(n) where n is the width of a number
        - find function traverses through items making it O(n)
        - if load factor > .75, the resize method creates a new linkedlist making it O(n)
        """
        new_set = Set(len(self))
        for item in self:
            new_set.add(item)
        for item in other_set:
            new_set.add(item)
        return new_set

    def intersection(self, other_set):
        """
        Returns new_set that is the intersection of this set and other_set

        Running time: O(4n + 4m) => O(n) or O(m)
        n = original set entries 
        m = other_set entries

        - traverses through each item in self making it O(n)
        - traverses through each item in other_set making it O(m)

        add func: O(3n + 3m)
        - hash funciton in bucket index is O(n) where n is the width of a number
        - find function traverses through items making it O(n)
        - if load factor > .75, the resize method creates a new linkedlist making it O(n)
        """
        new_set = Set(len(self))
        for item in self: # O(n)
            # if other_set.contains(item): # O(2m)
            if item in other_set: # O(m)
                new_set.add(item) # O(2n)
        return new_set

    def difference(self, other_set):
        """
        Returns new_set that is the difference of this set and other_set

        Running time: O(4n + 4m) => O(n) or O(m)
        n = original set entries 
        m = other_set entries

        - traverses through each item in self making it O(n)
        - traverses through each item in other_set making it O(m)

        set func: O(3n + 3m)
        - hash funciton in bucket index is O(n) where n is the width of a number
        - find function traverses through items making it O(n)
        - if load factor > .75, the resize method creates a new linkedlist making it O(n)
        """
        new_set = Set(len(self))
        for item in self: # O(n)
            if item not in other_set: # O(m)
                new_set.set(item) # O(2n)
        return new_set

    def is_subset(self, other_set):
        """
        Returns a boolean indicating whether other_set is a subset of this set

        Running time: O(4n + 4m) => O(n) or O(m)
        n = original set entries 
        m = other_set entries

        - traverses through each item in self making it O(n)
        - traverses through each item in other_set making it O(m)

        set func: O(3n + 3m)
        - hash funciton in bucket index is O(n) where n is the width of a number
        - find function traverses through items making it O(n)
        - if load factor > .75, the resize method creates a new linkedlist making it O(n)
        """
        for item in self: # O(n)
            if item not in other_set: # O(m)
                return False
        return True

def test_set():
    test = Set()
    print('Set: ' + str(test))

    print('Setting entries:')
    test.add('S')
    print('set(S): ' + str(test))
    test.add('A')
    print('set(A): ' + str(test))
    test.add('F')
    print('set(F): ' + str(test))
    test.add('E')
    print('set(E): ' + str(test))
    # print('Set: ' + str(test))
    print('size: ' + str(test.size) + '\n')

    print('Checking entries:')
    print('contains(S): ' + str(test.contains('S')))
    print('contains(A): ' + str(test.contains('A')))
    print('contains(F): ' + str(test.contains('F')))
    print('contains(E): ' + str(test.contains('E')))
    print('')

    print('Removing entries:')
    test.remove('S')
    print('remove(S): ' + str(test))
    test.remove('A')
    print('remove(A): ' + str(test))
    test.remove('F')
    print('remove(F): ' + str(test))
    test.remove('E')
    print('remove(E): ' + str(test))
    print('contains(F): ' + str(test.contains('F')))
    print('size: ' + str(test.size))

if __name__ == '__main__':
    test_set()