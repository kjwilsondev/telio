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

    def __iter__(self):
        """
        Iterates through nodes
        """
        # return 'LinkedList({!r})'.format(self.generator())
        return self.generator()

    def generator(self):
        """
        Returns node data
        """
        # Initialize node to first node
        node = self.head
        # Traverse through node list
        while node is not None:
            # https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/
            # yield in order to have multiple returns
            yield node.data
            node = node.next

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
        O(n) when traversal is neccessary
        (especially the second to last item!)
        """
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))

        # TODO: Make if statements that finds whether index is closer to head or tail
        #       in order to traverse forwards or backwards

        # Avoiding traversal if item is easily accessible
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
        O(1) - when index is 0 or the length of the linked list

        Worst case running time: 
        O(n) - traversing through n-1 items
        """
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))

        # New node initialized
        new_node = Node(item)

        # Avoiding traversal if item is easily accessible
        if index == 0:
            # new_node.next = self.head
            # self.head = new_node
            return self.prepend(item)

        if index == self.size:
            # self.tail.next = new_node
            # new_node.previous = self.tail
            # self.tail = new_node
            return self.append(item)

        # TODO: Make if statements that finds whether index is closer to head or tail
        #       in order to traverse forwards or backwards

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
        # Add to size
        self.size += 1

        # Node has been inserted to linked list!
        return

    def append(self, item):
        """
        Inserts the given item at the tail of linked list

        Best and worst case running time: 
        O(1) because there is no traversal - strictly changing attributes
        """
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
        """
        Insert the given item at the head of this linked list.

        Best and worst case running time: 
        O(1) because there is no traversal - strictly changing attributes
        """
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign tail to new node
            self.tail = new_node
        else:
            # Otherwise insert new node before head
            new_node.next = self.head
            self.head.previous = new_node

        # Update head to new node regardless
        self.head = new_node
        self.size += 1

    def find(self, quality):
        """
        Returns an item from this linked list satisfying the given quality.
        
        Best case running time: 
        Omega(1) if item is near the head of the list.
        
        Worst case running time: 
        O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list
        """
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
        """
        Find the node containing the given old_item
        replace data with new_item, without creating a new node object
        or
        raise ValueError if old_item is not found

        Best case running time: 
        O(1) - when index is 0 or the length of the linked list

        Worst case running time: 
        O(n) - traversing through n-1 items
        """
        # Start at the head node
        node = self.head
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:
            # Check if this node's data satisfies the given quality function
            if node.data == old_item:
                # Change node data to new_item
                node.data = new_item
                return
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # We never found data satisfying quality, but have to return something
        raise ValueError('Value not found: {}'.format(old_item))  # Constant time to return None

    def delete(self, item):
        """
        Delete the given item from this linked list, or raise ValueError.
        
        Best case running time: 
        O(1) - when index is 0 or the length of the linked list

        Worst case running time: 
        O(n) - traversing through n-1 items
        """

        # Start at the head node
        node = self.head
        # Keep track of the node before the one containing the given item
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
                node = node.next
        # Check if we found the given item or we never did and reached the tail
        if found:
            self.size -= 1
            # Check if we found a node in the middle of this linked list
            if node is not self.head and node is not self.tail:
                # Update the previous node to skip around the found node
                node.previous.next = node.next
                node.next.previous = node.previous
                # Unlink the found node from its next node
                node.next = None
                node.previous = None
                return
            # Check if we found a single node in linked list
            if node is self.head and node is self.tail:
                self.head = None
                self.tail = None
                return
            # Check if we found a node at the head and tail
            if node is self.head:
                # Update head to the next node
                self.head = node.next
                # Unlink the found node from the next node
                node.next.previous = None
                node.next = None
            # Check if we found a node at the tail
            if node is self.tail:
                # Check if there is a node before the found node
                if node.previous is not None:
                    # Unlink the previous node from the found node
                    node.previous.next = None
                    self
                # Update tail to the previous node regardless
                # Unlink node from list
                self.tail = node.previous
                node.previous.next = None
                node.previous = None
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

    # print('Getting items by index:')
    # for index in range(ll.size):
    #     item = ll.get_at_index(index)
    #     print('get_at_index({}): {!r}'.format(index, item))

    # TESTING ITERABLE
    print('Getting items by index:')
    for index, item in enumerate(ll):
        item = ll.get_at_index(index)
        print('get_at_index({}): {!r}'.format(index, item))

    print('Deleting items:')
    ll.delete('B')
    print(ll)
    print('size: {}'.format(ll.size))
    ll.delete('C')
    print(ll)
    print('size: {}'.format(ll.size))
    ll.delete('A')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))



if __name__ == '__main__':
    test_linked_list()