#!python
# -*- coding: utf-8 -*-

from linkedlist import LinkedList

# Using doubly linked list so the linked queue orientation doesnt matter

# Trouble shooting
# SyntaxError: Non-ASCII character '\xe2' in file
# with open("queue.py") as fp:
#     for i, line in enumerate(fp):
#         if "\xe2" in line:
#             print i, repr(line)

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
        """
        Returns a string representation of this queue
        """
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """
        Return True if this queue is empty
        or
        False, if otherwise
        """
        # Check if empty
        return self.list.size == 0

    def length(self):
        """
        Returns the number of items in this queue
        """
        return self.list.size


    def enqueue(self, item):
        """
        Inserts the given item at the back of this queue.

        Running time: O(1) – Function prepend does not traverse through items
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
        # Remove and return front item, if any
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
        self.size = 0
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """
        Returns a string representation of this queue
        """
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """
        Returns True if this queue is empty, or False otherwise
        """
        # Check if empty
        return self.size == 0

    def length(self):
        """
        Returns the number of items in this queue
        """
        # Count number of items
        return self.size

    def enqueue(self, item):
        """
        Inserts the given item at the back of this queue

        Running time: O(n) – insert function requires traversal of indexes
        https://wiki.python.org/moin/TimeComplexity
        """
        # Insert given item
        self.size += 1
        return self.list.insert(0, item)

    def front(self):
        """
        Returns the item at the front of this queue without removing it
        or 
        None if this queue is empty
        """
        # Return front item, if any
        if self.is_empty():
            return None
        return self.list[self.size - 1]

    def dequeue(self):
        """
        Remove and return the item at the front of this queue
        or 
        raise ValueError if this queue is empty

        Running time: O(1) – pop function does not require traversal
        """
        # Remove and return front item, if any
        if self.is_empty():
            raise ValueError('Stack is empty')
        self.size -= 1
        return self.list.pop()

class Deque(LinkedQueue):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def push_front(self, item):
        """
        Inserts the given item in front of queue

        Running time: O(1) – Function prepend does not traverse through items
        """
        # Push given item
        return self.list.append(item)

    def push_back(self, item):
        """
        Inserts the given item in back of queue

        Running time: O(1) – Function prepend does not traverse through items
        """
        # Push given item
        return self.list.prepend(item)

    def pop_front(self):
        """
        Removes and returns the item at the front of this queue,
        or 
        raises ValueError if this queue is empty

        Running time: O(1) – Returns tail data then dips
        """
        # Remove and return front item, if any
        if self.is_empty():
            raise ValueError('Queue is empty')
        data = self.list.tail.data
        self.list.tail = self.list.tail.previous
        self.list.size -= 1
        return data

    def pop_back(self):
        """
        Removes and returns the item at the back of this queue,
        or 
        raises ValueError if this queue is empty

        Running time: O(1) – Returns head data then dips
        """
        # Remove and return front item, if any
        if self.is_empty():
            raise ValueError('Queue is empty')
        data = self.list.head.data
        self.list.head = self.list.head.next
        self.list.size -= 1
        return data


# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
# Queue = LinkedQueue
# Queue = ArrayQueue
Queue = Deque