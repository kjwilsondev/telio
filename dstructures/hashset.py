#!python

from linkedlist import LinkedList

# Reworked Hash Table to store one item
# rather than storing tuples

class HashSet(object):

    def __init__(self, init_size=16, elements=None):
        """Initializes this hash set with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]
        self.size = 0  # Number of key-value entries
        if elements is not None:
            for item in elements:
                self.set(item)

    def __str__(self):
        """Returns a formatted string representation of this hash set"""
        items = ['item: {!r}'.format(item) for item in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Returns a string representation of this hash set"""
        return 'HashSet({!r})'.format(self.items())

    def _bucket_index(self, item):
        """Returns the bucket index where the given key would be stored."""
        return hash(item) % len(self.buckets)

    def __iter__(self):
        """
        Iterates through items in set
        """
        return self._generator()

    def _generator(self):
        """
        Returns items in set
        """
        for item in self.items():
            yield item

    def load_factor(self):
        """
        Returns the load factor, the ratio of number of entries to buckets.

        Running time: O(1) - divides attributes
        """
        # Calculate load factor
        return float(self.size) / float(len(self.buckets))

    def items(self):
        """
        Returns a list of all entries (key-value pairs) in this hash table.

        Running time: O(n) - traverses through all buckets to retrieve key, value pairs
        """
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        self.size = 0
        for bucket in self.buckets:
            all_items.extend(bucket.items())
            self.size += 1
        return all_items

    def length(self):
        """
        Returns the number of key-value entries by traversing its buckets.

        Running time: O(1) - returns size attribute
        """
        return self.size

    def contains(self, item):
        """
        Returns True if this hash table contains the given key
        or 
        False

        Running time: O(2n) => O(n)
        - hash funciton in bucket index is O(n) where n is the width of a number
        - find function traverses through key values making it O(n)
        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(item) # O(n)
        bucket = self.buckets[index] # O(1)
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda item_value: item_value == item) # O(n)
        return entry is not None  # True or False

    def get(self, item):
        """
        Returns the value associated with the given item
        or 
        raise KeyError

        Running time: O(2n) => O(n)
        - hash funciton in bucket index is O(n) where n is the width of a number
        - find function traverses through items making it O(n)
        """
        # Find the bucket the given item belongs in
        index = self._bucket_index(item) # O(n)
        bucket = self.buckets[index] # O(1)
        # Find the entry with the given item in that bucket, if one exists
        entry = bucket.find(lambda item_value: item_value[0] == item) # O(n)
        if entry is not None:  # Found
            # Return the given item's associated value
            return entry
        else:  # Not found
            raise KeyError('Item not found: {}'.format(item))

    def set(self, item):
        """
        Inserts or updates the given item

        Running time: O(3n) => O(n)
        - hash funciton in bucket index is O(n) where n is the width of a number
        - find function traverses through items making it O(n)
        - if load factor > .75, the resize method creates a new linkedlist making it O(n)
        """
        # Find the bucket the given item belongs in
        index = self._bucket_index(item) # O(n)
        bucket = self.buckets[index] # O(1)
        # Find the entry with the given item in that bucket, if one exists
        # Check if an entry with the given item exists in that bucket
        entry = bucket.find(lambda item_value: item_value[0] == item)
        if entry is not None:  # Found
            # In this case, the given item is being updated
            # Remove the old item entry from the bucket first
            bucket.delete(entry) # O(n)
            self.size -= 1
        # Insert the new item entry into the bucket in either case
        bucket.append(item)
        self.size += 1
        # Check if the load factor exceeds a threshold such as 0.75
        if self.load_factor() > 0.75:
            # If so, automatically resize to reduce the load factor
            self._resize() # O(n)

    def delete(self, item):
        """
        Deletes the given item
        or 
        raise KeyError

        Running time: O(2n) => O(n)
        - hash funciton in bucket index is O(n) where n is the width of a number
        - find function traverses through items making it O(n)
        """
        # Find the bucket the given item belongs in
        index = self._bucket_index(item)
        bucket = self.buckets[index]
        # Find the entry with the given item in that bucket, if one exists
        entry = bucket.find(lambda item_value: item_value[0] == item)
        if entry is not None:  # Found
            # Remove the item entry from the bucket
            bucket.delete(entry) # O(n)
            self.size -= 1
        else:  # Not found
            raise KeyError('Item not found: {}'.format(item))

        # If the hash table is close to empty 
        # then divide the size of hash table in half by passing in 0
        # if self.load_factor() > 0.2:
        #     # If so, automatically resize to reduce the load factor
        #     self._resize(0) # O(n)

    def _resize(self, new_size=None):
        """
        Resizes the hash set buckets and rehashes all entries.
        Called automatically when load factor exceeds a threshold
        such as 0.75 after an insertion (when set is called with a new key)

        Running time: O(6n) => O(n)
        - self.items() traverses through all of entries making it O(n)
        - self.buckets creates an array of double the amount of linkedlists 
          as entries making it O(2n)
        - set funciton which hashes each item is O(3n)
        """
        # If unspecified, choose new size dynamically based on current size
        if new_size is None:
            new_size = len(self.buckets) * 2  # Double size 
        # Option to reduce size if buckets are sparsely filled (low load factor)
        elif new_size is 0:
            new_size = len(self.buckets) / 2  # Half size
        # Get a list to temporarily hold all current key-value entries
        entries = self.items() # O(n)
        # Create a new list of new_size total empty linked list buckets
        self.buckets = [LinkedList() for i in range(new_size)] # O(n)
        self.size = 0
        # Insert each key-value entry into the new list of buckets,
        # which will rehash them into a new bucket index based on the new size
        for item in entries:
            self.set(item)


# if __name__ == '__main__':