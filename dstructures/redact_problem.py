#!python3
from hashset import HashSet

def redact(speech, banned):
    off_limits = HashSet()
    for word in banned:
        off_limits.set(word.lower())

    new_speech = [word for word in speech if not off_limits.contains(word)]
    # new_speech = []
    # for word in speech:
    #     if not off_limits.contains(word):
    #         new_speech.append(word)
    
    return new_speech

if __name__ == '__main__':
    print(redact(['I', 'hate', 'noise'], ['noise']))
