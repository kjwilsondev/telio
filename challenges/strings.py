#!python3

def contains(text, pattern, letter=None, patterndex=0):
    """
    Recursive Implementation
    Return a boolean indicating whether pattern occurs in text.
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # Initialize values
    if letter is None:
        letter = 0

    if patterndex == len(pattern):
        print("yup !!")
        return True
    
    # Skips over letters 
    # that dont match first letter of pattern
    while text[letter] != pattern[patterndex]:
        letter += 1
        if letter >= len(text) - 1:
            print("nope")
            return False
    
    # Checks if next letter in text
    # matches the next letter in the pattern
    if text[letter] != pattern[patterndex]:
        # if not sends it back to while loop with new start
        return contains(text, pattern, letter)
    return contains(text, pattern, letter+1, patterndex+1)


def find_index(text, pattern, letter=None, patterndex=0):
    """
    Recursive Implementation
    Returns the starting index of the first occurrence of pattern in text,
    or None if not found.
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    
    # Initialize values
    if letter is None:
        letter = 0

    if patterndex == len(pattern):
        print("yup !!!")
        print(letter-patterndex)
        return letter - patterndex
    
    # Skips over letters 
    # that dont match first letter of pattern
    while text[letter] != pattern[patterndex]:
        letter += 1
        if letter >= len(text) - 1:
            print("nope")
            return None
    
    # Checks if next letter in text
    # matches the next letter in the pattern
    if text[letter] != pattern[patterndex]:
        # if not sends it back to while loop with new start
        return find_index(text, pattern, letter)
    return find_index(text, pattern, letter+1, patterndex+1)


def find_all_indexes(text, pattern):
    """
    Iterative Implementation
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Initialize values and index array
    indarray = []
    patterndex = 0

    # File through each letter in text
    for i, letter in enumerate(text):
        # if letter match is found
        if letter == pattern[patterndex]:
            patterndex += 1
        else:
            patterndex = 0
        # if pattern index reaches full length
        # pattern was found !
        if patterndex == len(pattern):
            indarray.append(i - (len(pattern) - 1))
            patterndex = 0

    # Returns index array
    return indarray




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
    # main()
    find_all_indexes('kdjasldjf;alksdjf;alksjdf;laksjdfl;kajsd;flkjas;dlfkjas;ldfjk', 'kj')