#!python3
# to run pytest:
# python3 -m pytest bases_test.py

import string
from decimal import Decimal
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
    return: int or float representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Return integer
    answer = 0

    # Digits length
    dlength = len(digits) - 1
    letters = "0123456789abcdefghijklmnopqrstuvwxyz"
    
    # Fraction detection
    if "." in digits:
        digits, fractions = digits.split(".")
        # print(f"digits: {digits}")
        # print(f"fractions: {fractions}")
        dlength = len(digits) - 1
        # flength = len(fractions) - 1
        f = 1

        answer = float(answer)
        print(f"1 answer: {answer}")
        # print(f"before fraction: {answer}")
        for number in fractions:
            print(f"1 number: {number}")
            # if letter gives numeric value
            if number.isalpha():
                number = letters.index(number)
                print(f"2 number: {number}")
            number = int(number)
            print(f"2 answer: {answer}")
            print(f"3 number: {number}")
            # get rid of superfluous zeroes
            result = str(number * (base ** -f))
            result = float(result.strip('0'))
            # encoding in base 10 gives trailing zeroes :(
            answer += result
            print(f"3 answer: {answer}")
            f += 1

    # Decodes digits from any base (2 up to 36)
    for number in digits:
        # if letter gives numeric value
        if number.isalpha():
            number = letters.index(number)
        number = int(number)
        answer += number * (base ** dlength)
        dlength -= 1

    print(f"base 10: {answer}")
    return answer


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int or float representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    # assert number >= 0, 'number is negative: {}'.format(number)
    # Handle numbers above 255
    # assert number <= 255, 'number must be below 255: {}'.format(number)

    # Encodes number to binary (base 2)
    # if base is 2:
        # Cheating using f string
        # return '{0:08b}'.format(number)

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

        # print(answer)
        # return answer
        
    # Encodes number in hexadecimal (base 16)
    # if base is 16:
        # Cheating using f string
        # return '{:x}'.format(number)

    # Encodes number in any base (2 up to 36)

    answer = ""
    decimal = ""
    letters = "0123456789abcdefghijklmnopqrstuvwxyz"
    # Turn number back into string to detect fraction
    digit = number
    number = str(number)
    fraction = False

    # Fraction detection
    if "." in number:
        fraction = True
        digit, part = number.split(".")
        # print(f"digits: {digits}")
        # print(f"fractions: {fractions}")
        digit = int(digit)
        part = float("." + part)
        found = False
        okjuststop = False

        while not found:
            part *= base
            intpart = int(part)
            part -= intpart
            if intpart >= 10:
                intpart = letters[intpart]
            decimal += str(intpart)
            print(part)
            if part == 0:
                found = True
            
            print("trying to get 1")
            okjuststop += 1

            # stops while loop for endless decimal
            if okjuststop > 50:
                found = True

    while digit > 0:
        # print(int(number % base))
        mod = str(digit % base)
        intmod = int(mod)
        # if mod over 10 gives alpha value
        if intmod >= 10:
            mod = letters[intmod]
        answer += mod
        digit = digit // base

    # Reverses list or string
    answer = answer[::-1]
    # Adds decimal to answer
    if fraction:
        # Dont put decimal if its just zero
        if not decimal == "0":
            answer += "." + decimal

    # TODO: make negative number function
    # ATTEMPTED TO ENCODE NEGATIVE NUMBERS
    # checks if number is negative
    # if float(number) > 0:
            
    print(f"base {base}: {answer}")
    return answer

def encodeNegative(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int or float representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    # Encodes number in any base (2 up to 36)

    answer = ""
    decimal = ""
    letters = "0123456789abcdefghijklmnopqrstuvwxyz"
    # Turn number back into string to detect fraction
    digit = number
    number = str(number)
    fraction = False

    # Fraction detection
    if "." in number:
        fraction = True
        digit, part = number.split(".")
        # print(f"digits: {digits}")
        # print(f"fractions: {fractions}")
        digit = int(digit)
        part = float("." + part)
        found = False
        okjuststop = False

        while not found:
            part *= base
            intpart = int(part)
            part -= intpart
            if intpart >= 10:
                intpart = letters[intpart]
            decimal += str(intpart)
            print(part)
            if part == 0:
                found = True
            
            print("trying to get 1")
            okjuststop += 1

            # stops while loop for endless decimal
            if okjuststop > 50:
                found = True

    while digit > 0:
        # print(int(number % base))
        mod = str(digit % base)
        intmod = int(mod)
        # if mod over 10 gives alpha value
        if intmod >= 10:
            mod = letters[intmod]
        answer += mod
        digit = digit // base

    # Reverses list or string
    answer = answer[::-1]
    # Adds decimal to answer
    if fraction:
        # Dont put decimal if its just zero
        if not decimal == "0":
            answer += "." + decimal

    # TODO: make negative number function
    # ATTEMPTED TO ENCODE NEGATIVE NUMBERS
    # checks if number is negative
    # if float(number) > 0:
            
    print(f"base {base}: {answer}")
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

    # Converts digits from any base to any base (2 up to 36)
    # Decodes number from original base to base 10
    # print("decoding:")
    number = decode(digits, base1)
    # Encodes number to desired base
    # print("encoding:")
    # print(encode(number, base2))
    return encode(number, base2)
    # returns string result
    # print(answer)
    # return answer


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    # decode(sys.argv[1], int(sys.argv[2]))
    # encode(float(sys.argv[1]), int(sys.argv[2]))
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