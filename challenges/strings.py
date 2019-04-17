#!python3

# TODO: Permutation Finder

def contains(text, pattern, letter=None, patterndex=0):
    """
    Return a boolean indicating whether pattern occurs in text.

    Running time: O(n) – in transverses through list of characters in text
    https://stackoverflow.com/questions/13884177/complexity-of-in-operator-in-python
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if pattern in text:
        return True
    return False


def find_index(text, pattern, letter=None, patterndex=0):
    """
    Recursive Implementation
    Returns the starting index of the first occurrence of pattern in text,
    or None if not found.

    Running time: O(n) – find_all_indexes func is O(n)
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    indices = find_all_indexes(text, pattern)
    if len(indices) > 0:
        print(indices)
        return indices[0]
    return None


def find_all_indexes(text, pattern):
    """
    Iterative Implementation

    Running time: O(n) – for loop tranverses through text characters
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # FIRST ATTEMPT
    # File through each letter in text
    # for i, letter in enumerate(text):
    #     print(i, letter)
    #     # if letter match is found
    #     if letter == pattern[patterndex]:
    #         patterndex += 1
    #     # shamelessly hardcoding edgecase >:)
    #     elif letter == pattern[0]:
    #         patterndex = 1
    #     else:
    #         patterndex = 0
    #     # if pattern index reaches full length
    #     # pattern was found !
    #     print(patterndex)
    #     if patterndex == len(pattern):
    #         indarray.append(i - (len(pattern) - 1))
    #         patterndex = 0

    # 
    # Initialize index array
    indices = []

    # Empty string
    if pattern == "":
        print("Empty Pattern")
        for index, letter in enumerate(text):
            indices.append(index)
        return indices
    
    # Class Implementation
    # https://github.com/lvreynoso/CS1.3-Coursework/blob/master/strings.py
    indices = []
    candidates = {}
    delta = len(pattern)
    for position, character in enumerate(text):
        # find match all the first letters of the pattern
        if character == pattern[0]:
            candidates[position] = 1
        for index, streak in candidates.items():
            if streak != False:
                if index != position and character == pattern[streak]:
                    candidates[index] += 1
                elif index != position and character != pattern[streak]:
                    candidates[index] = False
                if candidates[index] == delta:
                    indices.append(index)
                    candidates[index] = False
    print(indices)
    return indices

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()

    # Tests
    # contains('abc', 'ac')
    # False
    # find_all_indexes('aaa', 'aa')
    # [0, 1]
    # find_index('abc', 'ac')
    # None