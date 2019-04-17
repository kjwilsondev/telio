"""Autocomplete Dictionary Input Challenge"""

import sys
import itertools

def load(text):
    """
    Loads words from dictionary
    """
    # Timo dictionary pull shortcut
    # wordList = [line.strip() for line in open('/usr/share/dict/words')]

    file  = open(text, 'r')
    loads = file.readlines()
    words = [word.strip() for word in loads]
    # equivalent to:
    # words2 = []
    # for word in words:
    #     words2.append(word.strip())

    file.close()
    return words

def anagram(word, text):
    """
    Adds anagrams from dictionary from input
    Stops game if no words found
    """
    # initializes word list of all possible anagrams
    gibberish = ["".join(perm) for perm in itertools.permutations(word)]
    anagrams  = []

    # iterates through text to find matches
    for perm in gibberish:
        for line in text:
            # print(perm)
            if (line == perm):
                anagrams.append(line)

    # no anagrams found
    if len(anagrams) == 0:
        print("No words found!")
        sys.exit(1)

    return anagrams

def game():
    print("\nWelcome to Anagram\n")

    word = input("Give me a word\n\n")
    # checks emptiness
    if not word:
        print("You must enter a word\n")
        sys.exit(1)

    loads    = load("/usr/share/dict/words")
    anagrams = anagram(str(word), loads)
    print("{} anagrams were found".format(len(anagrams)))
    print(anagrams)
    
    # c = 0
    
    # while c < results:
    #     sentence = "    {}.    {}".format((count + 1), anagrams[count])
    #     print(sentence)
    #     count += 1

if __name__ == '__main__':
    game()
    
    # anagrams = ["".join(perm) for perm in itertools.permutations("blue")]
    # print(len(anagrams))
    # print(anagrams[0])
    # print(anagrams[8])
    # text = ["cool", "lube", "work"]
    # l = list()
    # for perm in anagrams:
    #     for line in text:
    #         if line == (perm):
    #             l.append(line)

    # print(l)