#!python

class Node(object):

    def __init__(self, data):
        """
        Initializes this node with the given data
        """
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, iterable=None):
        """
        Initializes this linked list and append the given items, if any
        """
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes
        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """
        Returns a formatted string representation of this linked list
        """
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """
        Returns a string representation of this linked list
        """
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """
        Returns a list of all items in this linked list.

        Best and worst case running time: 
        Theta(n) for n items in the list
        because we always need to loop through all n nodes
        """
        # Create an empty list of results
        result = []  # Constant time to create a new list
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Always n iterations because no early exit
            # Append this node's data to the results list
            result.append(node.data)  # Constant time to append to a list
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # Now result contains the data from all nodes
        return result  # Constant time to return a list

    def is_empty(self):
        """
        Returns True if this linked list is empty, or False
        """
        return self.head is None # Constant time to access self.head

    def length(self):
        """
        Return the length of this linked list

        Best and worst case running time: 
        O(1) because function is only accessing size attribute
        """
        return self.size # Constant time to access self.size

    def get_at_index(self, index):
        """
        Finds the node at the given index and return its data
        or
        raises ValueError if the given index is out of range of the list size

        Best case running time: 
        O(1) if index is head or tail

        Worst case running time: 
        O(n) when transversal is neccessary
        (especially the second to last item!)
        """
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))

        # TODO: Make if statements that finds whether index is closer to head or tail
        #       in order to transverse forwards or backwards

        # Avoiding transversal if item is easily accessible
        if index == 0:
            return self.head.data
        if index == (self.size - 1):
            return self.tail.data

        # Node counter initialized to index
        node_count = index
        # Start at the head node
        node = self.head
        # Loops until the node is at target index
        while node_count > 0:
            # Skip to the next node
            node = node.next
            data = node.data
            # Count down
            node_count -= 1
        # Now node_count contains the number of nodes
        return data

    def insert_at_index(self, index, item):
        """
        Finds the node before the given index and inserts item after it
        or
        raises ValueError if the given index is out of range of the list size

        Best case running time: 
        ??? under what conditions? [TODO]

        Worst case running time: 
        ??? under what conditions? [TODO]
        """
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))

        # New node initialized
        new_node = Node(item)

        # Avoiding transversal if item is easily accessible
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        if index == (self.size - 1):
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
            return

        # TODO: Make if statements that finds whether index is closer to head or tail
        #       in order to transverse forwards or backwards

        # Node counter initialized to index - 1
        node_count = index - 1
        # Start at the head node
        old_node = self.head
        next_node = None
        # Loops until the node is at target index
        while node_count > 0:
            # Skip to the next node
            old_node = old_node.next
            next_node = old_node.next
            # Count down
            node_count -= 1
        
        # Set new node's next to next node
        new_node.next = next_node
        # Set next node's previous to new node
        next_node.previous = new_node
        # Set new node's previous to old node
        new_node.previous = old_node
        # Lastly, set old node's next to new node
        old_node.next = new_node

        # Node has been inserted to linked list!
        return

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Best and worst case running time: 
        O(1) [TODO]"""
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign head to new node
            self.head = new_node
        else:
            # Otherwise insert new node after tail
            self.tail.next = new_node
            new_node.previous = self.tail
        # Update tail to new node regardless
        self.tail = new_node
        self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Best and worst case running time: ??? under what conditions? [TODO]"""
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign tail to new node
            self.tail = new_node
        else:
            # Otherwise insert new node before head
            new_node.next = self.head
            self.head.previous = new_node.next

        # Update head to new node regardless
        self.head = new_node
        self.size += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Up to n iterations if we don't exit early
            # Check if this node's data satisfies the given quality function
            if quality(node.data):  # Constant time to call quality function
                # We found data satisfying the quality function, so exit early
                return node.data  # Constant time to return data
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # We never found data satisfying quality, but have to return something
        return None  # Constant time to return None

    def replace(self, old_item, new_item):
        """Replace the given old_item in this linked list with given new_item
        using the same node, or raise ValueError if old_item is not found.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # TODO: Find the node containing the given old_item and replace its
        # data with new_item, without creating a new node object
        pass

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Start at the head node
        node = self.head
        # Keep track of the node before the one containing the given item
        previous = None
        # Create a flag to track if we have found the given item
        found = False
        # Loop until we have found the given item or the node is None
        while not found and node is not None:
            # Check if the node's data matches the given item
            if node.data == item:
                # We found data matching the given item, so update found flag
                found = True
            else:
                # Skip to the next node
                previous = node
                node = node.next
        # Check if we found the given item or we never did and reached the tail
        if found:
            # Check if we found a node in the middle of this linked list
            if node is not self.head and node is not self.tail:
                # Update the previous node to skip around the found node
                previous.next = node.next
                # Unlink the found node from its next node
                node.next = None
            # Check if we found a node at the head
            if node is self.head:
                # Update head to the next node
                self.head = node.next
                # Unlink the found node from the next node
                node.next = None
            # Check if we found a node at the tail
            if node is self.tail:
                # Check if there is a node before the found node
                if previous is not None:
                    # Unlink the previous node from the found node
                    previous.next = None
                # Update tail to the previous node regardless
                self.tail = previous
        else:
            # Otherwise raise an error to tell the user that delete has failed
            raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    print('Getting items by index:')
    for index in range(ll.size):
        item = ll.get_at_index(index)
        print('get_at_index({}): {!r}'.format(index, item))

    print('Deleting items:')
    ll.delete('B')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('A')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()