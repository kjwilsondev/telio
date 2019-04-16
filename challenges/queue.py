#!python

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """
        Return True if this queue is empty
        or
        False, if otherwise
        """
        # Check if empty
        print("WE MADE IT")
        print(self.list.size == 0)
        return self.list.size == 0

    def length(self):
        """Return the number of items in this queue."""
        return self.list.size


    def enqueue(self, item):
        """
        Inserts the given item at the back of this queue.

        Running time: O(1) – Function prepend does not transverse through items
        """
        # Insert given item
        return self.list.prepend(item)


    def front(self):
        """
        Returns the item at the front of this queue without removing it
        or 
        None if this queue is empty
        """
        # Returns front item, if any
        if self.is_empty():
            return None
        return self.list.tail.data

    def dequeue(self):
        """
        Removes and returns the item at the front of this queue,
        or 
        raises ValueError if this queue is empty

        Running time: O(1) – Returns tail data then dips
        """
        # TODO: Remove and return front item, if any
        if self.is_empty():
            raise ValueError('Queue is empty')
        data = self.list.tail.data
        self.list.tail = self.list.tail.previous
        self.list.size -= 1
        return data


# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # TODO: Check if empty

    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Insert given item

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return front item, if any


# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
Queue = LinkedQueue
# Queue = ArrayQueue