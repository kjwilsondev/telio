#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """
        Returns a string representation of this stack
        """
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """
        Returns True if this stack is empty, or False otherwise
        """
        # Checks if head is empty
        return self.list.head is None

    def length(self):
        """
        Returns the number of items in this stack
        """
        # Count number of items
        return self.list.size

    def push(self, item):
        """
        Inserts the given item on the top of this stack

        Running time: O(1) – Function prepend does not transverse through items
        """
        # Push given item
        return self.list.prepend(item)

    def peek(self):
        """
        Returns the item on the top of this stack without removing it,
        or 
        None if this stack is empty
        """
        # Return top item, if any
        if self.list.is_empty():
            return None
        return self.list.head.data

    def pop(self):
        """
        Removes and returns the item on the top of this stack,
        or 
        raises ValueError if this stack is empty.

        Running time: O(1) – Returns head data then dips
        """
        # Remove and return top item, if any
        if self.list.is_empty():
            return None
        yield self.list.head.data
        self.list.head = self.list.head.next
        self.list.size -= 1


# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """
        Returns a string representation of this stack
        """
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """
        Returns True if this stack is empty
        or 
        False, if otherwise
        """
        # Check if empty
        return len(self.list) == 0

    def length(self):
        """
        Returns the number of items in this stack
        """
        # Count number of items
        return len(self.list)

    def push(self, item):
        """
        Inserts the given item on the top of this stack

        Running time: O(???) – Why? [TODO]"""
        # Insert given item
        return self.list.insert(0, item)

    def peek(self):
        """
        Returns the item on the top of this stack without removing it,
        or 
        None if this stack is empty
        """
        # Return top item, if any
        if self.list.is_empty():
            return None
        return self.list[0]


    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        # Remove and return top item, if any
        if self.list.is_empty():
            return None
        return self.list.pop(0)


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
# Stack = ArrayStack