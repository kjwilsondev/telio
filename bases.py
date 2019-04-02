#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Digits length
    length = len(digits) - 1
    # Return integer
    answer = 0

    # Decode digits from binary (base 2)
    if base is 2:
        for number in digits:
            number = int(number)
            answer += number * (base ** length)
            length -= 1
        return answer
    
    # TODO: Decode digits from hexadecimal (base 16)
    if base is 16:
        for number in digits:
            # if letter gives value
            if number.isalpha():
                if number is "a":
                    number = 10
                if number is "b":
                    number = 11
                if number is "c":
                    number = 12
                if number is "d":
                    number = 13
                if number is "e":
                    number = 14
                if number is "f":
                    number = 15
            
            number = int(number)
            print(number)
            answer += number * (base ** length)
            length -= 1
        print(answer)
        return answer

    # Decode digits from any base (2 up to 36)
    for number in digits:
        number = int(number)
        answer += number * (base ** length)
        length -= 1
    return answer


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # Handle numbers above 255
    assert number <= 255, 'number must be below 255: {}'.format(number)

    # Encode number in binary (base 2)
    # if base is 2:
    #     answer = [0, 0, 0, 0, 0, 0, 0 ,0]
    #     place = len(answer) - 1
    #     exponent = 0
    #     while number > 0:
    #         number = int(number)
    #         answer[place] = number
        
    # TODO: Encode number in hexadecimal (base 16)
    # ...
    # TODO: Encode number in any base (2 up to 36)
    # ...


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    decode(sys.argv[1], int(sys.argv[2]))
    # if len(args) == 3:
    #     digits = args[0]
    #     base1 = int(args[1])
    #     base2 = int(args[2])
    #     # Convert given digits between bases
    #     result = convert(digits, base1, base2)
    #     print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    # else:
    #     print('Usage: {} digits base1 base2'.format(sys.argv[0]))
    #     print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()