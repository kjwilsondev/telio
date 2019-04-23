from hashset import HashSet
from linkedlist import LinkedList

class Set(HashSet):

    def __init__(self, init_size=16, elements=None):
        """Initializes the set with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]
        self.size = 0  # Number of key-value entries
        if elements is not None:
            for item in elements:
                self.set(item)

    def contains(self, element):
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

    def union(self, other_set):
        """
        Returns a new set that is the union of this set and other_set

        Running time: O(4n + 4m) => O(n)
        n = original set entries 
        m = other_set entries

        - traverses through each item in self making it O(n)
        - traverses through each item in other_set making it O(m)

         set func: O(3n + 3m)
        - hash funciton in bucket index is O(n) where n is the width of a number
        - find function traverses through items making it O(n)
        - if load factor > .75, the resize method creates a new linkedlist making it O(n)
        """
        for 



    


# if __name__ == '__main__':