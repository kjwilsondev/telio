#!python3

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

# f string docs
# https://realpython.com/python-f-strings/


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

    # Decodes digits from binary (base 2)
    if base is 2:
        for number in digits:
            number = int(number)
            answer += number * (base ** length)
            length -= 1

        print(answer)
        return answer
    
    # Decodes digits from hexadecimal (base 16)
    if base is 16:
        for number in digits:
            # if letter gives value
            if number.isalpha():
                if number == "a":
                    number = 10
                if number == "b":
                    number = 11
                if number == "c":
                    number = 12
                if number == "d":
                    number = 13
                if number == "e":
                    number = 14
                if number == "f":
                    number = 15
            
            number = int(number)

            answer += number * (base ** length)
            length -= 1

        print(answer)
        return answer

    # Decodes digits from any base (2 up to 36)
    letters = "0123456789abcdefghijklmnopqrstuvwxyz"
    for number in digits:
        # if letter gives numeric value
        if number.isalpha():
            number = letters.index(number)
        number = int(number)
        answer += number * (base ** length)
        length -= 1

    print(answer)
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
    # assert number <= 255, 'number must be below 255: {}'.format(number)

    # Encodes number in binary (base 2)
    if base is 2:
        # Cheating using f string
        # return '{0:08b}'.format(number)
        answer = ""
        orig_numb = number
        while number > 0:
            # print(int(number % base))
            mod = str(number % base)
            answer += mod
            number = int(number / base)
        # Reverse list or string
        answer = answer[::-1]

        # Pad with 4n indexes for binary format
        # Had to highlight this out because pytest
        # if orig_numb > 15:
        #     answer = answer.zfill(8)
        # if orig_numb > 255:
        #     answer = answer.zfill(12)
        # if orig_numb > 4095:
        #     answer = answer.zfill(16)
        # if orig_numb > 65535:
        #     answer = answer.zfill(20)
        # else: 
        #     answer = answer.zfill(4)

        print(answer)
        return answer
        
    # Encodes number in hexadecimal (base 16)
    if base is 16:
        # Cheating using f string
        # return '{:x}'.format(number)
        answer = ""
        while number > 0:
            # print(int(number % base))
            mod = str(number % base)
            # if mod over 10 gives alpha value
            if int(mod) >= 10:
                if mod == "10":
                    mod = "a"
                if mod == "11":
                    mod = "b"
                if mod == "12":
                    mod = "c"
                if mod == "13":
                    mod = "d"
                if mod == "14":
                    mod = "e"
                if mod == "15":
                    mod = "f"
            answer += mod
            number = int(number / base)
        # Reverses list or string
        answer = answer[::-1]

        print(answer)
        return answer

    # Encodes number in any base (2 up to 36)
    answer = ""
    letters = "0123456789abcdefghijklmnopqrstuvwxyz"
    while number > 0:
        # print(int(number % base))
        mod = str(number % base)
        intmod = int(mod)
        # if mod over 10 gives alpha value
        if intmod >= 10:
            mod = letters[intmod]
        answer += mod
        number = int(number / base)
    # Reverses list or string
    answer = answer[::-1]
    print(answer)
    return answer


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handles up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # TODO: Convert digits from base 10 to base 16 (and vice versa)

    # Converts digits from any base to any base (2 up to 36)
    # Decodes number from original base to base 10
    # print("decoding:")
    number = decode(digits, base1)
    # Encodes number to desired base
    # print("encoding:")
    answer = encode(number, base2)
    # returns string result
    print(answer)
    return answer


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    # decode(sys.argv[1], int(sys.argv[2]))
    # encode(int(sys.argv[1]), int(sys.argv[2]))
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()