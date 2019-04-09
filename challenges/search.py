#!python3

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_recursive(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # if array is smaller than index
    # item was not found
    if (len(array) - 1) < index:
        return None
    # checks if item found
    if item == array[index]:
        print(index)
        return index
    # if not call function
    else:
        return linear_search_recursive(array, item, index + 1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # Edge Casing
    # if item > array[len(array)-1] or item < array[0]:
    #     return None
    # else:
        array = array.sort()
        print(array)
        return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    left = 0
    right = len(array) - 1
    while left <= right:
        # set median
        middle = (left + right) // 2
        print(f"middle: {middle}")
        val = array[middle]
        print(f"val: {val}")

        # check if item found
        if val == item:
            return middle
        if val < item:
            left = middle + 1
            print(f"new left: {left}")
        elif val > item:
            right = middle - 1
            print(f"new right: {right}")
    
    # returns None if not found
    return None
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # Implements binary search recursively here

    # if item > array[len(array)-1] or 0 > array[array[len(array)-1]]:
    #     return None
    
    # Initializes left and right
    if right == None:
        left = 0
        right = len(array) - 1

    # set median
    middle = (left + right) // 2
    val = array[middle]

    # check if item found
    if val == item:
        return middle
    if val < item:
        left = middle + 1
        return binary_search_recursive(array, item, left, right)
    elif val > item:
        right = middle - 1
        return binary_search_recursive(array, item, left, right)

    # returns None if not found
    return None
    
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    if len(args) == 1:
        array = ['Winnie', 'Kojin', 'Brian', 'Nabil', 'Julia', 'Alex', 'Nick']
        item = args[0]
        result = binary_search(array, item)
        print(f"Looked for {item} in {array}")
        print(f"It was found at {result}")
    else:
        print(f"Usage: item")

