#!python3

def contains(text, pattern, letter=None, patterndex=0):
    """
    Return a boolean indicating whether pattern occurs in text.
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # Recursive Implementation

    # # Initialize values
    # if letter is None:
    #     letter = 0

    # if patterndex == len(pattern):
    #     print(True)
    #     return True
    
    # # Skips over letters 
    # # that dont match first letter of pattern
    # while text[letter] != pattern[patterndex]:
    #     print(text[letter])
    #     letter += 1
    #     if letter >= len(text):
    #         print(False)
    #         return False
    
    # # Checks if next letter in text
    # # matches the next letter in the pattern
    # if text[letter] != pattern[patterndex]:
    #     # if not sends it back to while loop with new start
        
    #     return contains(text, pattern, letter)
    # return contains(text, pattern, letter+1, patterndex+1)

    if pattern in text:
        print(True)
        return True
    print(False)
    return False


def find_index(text, pattern, letter=None, patterndex=0):
    """
    Recursive Implementation
    Returns the starting index of the first occurrence of pattern in text,
    or None if not found.
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    
    # # Initialize values
    # if letter is None:
    #     letter = 0

    # if patterndex == len(pattern):
    #     print(letter-patterndex)
    #     return (letter - patterndex)
    
    # # Skips over letters 
    # # that dont match first letter of pattern
    # while text[letter] != pattern[patterndex]:
    #     letter += 1
    #     if letter >= len(text):
    #         print(None)
    #         return None
    
    # # Checks if next letter in text
    # # matches the next letter in the pattern
    # if text[letter] != pattern[patterndex]:
    #     # if not sends it back to while loop with new start
    #     return find_index(text, pattern, letter)
    # return find_index(text, pattern, letter+1, patterndex+1)

    indices = find_all_indexes(text, pattern)
    if len(indices) > 0:
        print(indices)
        return indices[0]
    return None


def find_all_indexes(text, pattern):
    """
    Iterative Implementation
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # # Initialize values and index array
    indarray = []
    # patterndex = 0

    # empty string
    if pattern == "":
        print("empty pattern")
        for index, letter in enumerate(text):
            indarray.append(index)
        return indarray
    
    # # File through each letter in text
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

    # # Returns index array
    # print(indarray)
    # return indarray
    indices = []
    candidates = {}
    delta = len(pattern)
    for position, character in enumerate(text):
        # try to match all the first letters of the pattern
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
    #main()
    contains('abc', 'ac')
    # False
    find_all_indexes('aaa', 'aa')
    # [0, 1]
    find_index('abc', 'ac')
    # None