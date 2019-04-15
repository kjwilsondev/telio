#!python3

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_recursive(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # Set indexes at opposite ends
    left = 0
    right = len(text) - 1

    punctuation = set(string.punctuation)

    # Loops until indexes meet
    while left <= right:
        # Ignore space and punctuation
        # https://www.dotnetperls.com/punctuation-python
        while text[left] == " " or text[left] in punctuation:
            left += 1
        while text[right] == " " or text[right] in punctuation:
            right -= 1
        # Check for match
        if text[left].lower() != text[right].lower():
            return False
        left += 1
        right -= 1
    return True


def is_palindrome_recursive(text, left=None, right=None):
    # fix text to pass test
    # text = text.lower()
    # text = text.translate(str.maketrans('','', string.punctuation))
    punctuation = set(string.punctuation)

    # Initializes indexes
    if right == None:
        left = 0
        right = len(text) - 1
    # Checks if indexes have met
    if left <= right:
        # Checks if index contains punctuation or space
        if text[left] == " " or text[left] in punctuation:
            return is_palindrome_recursive(text, left+1, right)
        if text[right] == " " or text[right] in punctuation:
            return is_palindrome_recursive(text, left, right-1)
        # Check if indexes are same (ignores caps)
        if text[left].lower() == text[right].lower():
            return is_palindrome_recursive(text, left+1, right-1)
        return False
    return True


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')

def refine_text(text):
    text = text.lower()
    exclusions = "?.-! ,'"
    for char in exclusions:
        text = text.replace(char, '')
    return text


if __name__ == '__main__':
    main()