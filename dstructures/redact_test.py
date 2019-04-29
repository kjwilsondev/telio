from redact_problem import redact
import unittest


class RedactTest(unittest.TestCase):
    def test_redacted_banned_words(self):
        # banned words list
        banned = ['lame', 'loser', 'bogus', 'weirdo', 'bozo']
        # redact function should take out banned words from array
        assert redact(['You', 'are', 'lame'], banned) == ['You', 'are']
        assert redact(['You', 'are', 'a', 'loser'], banned) == ['You', 'are', 'a']
        assert redact(['This', 'is', 'bogus'], banned) == ['This', 'is']
        assert redact(['Dont', 'be', 'a', 'weirdo', 'bozo'], banned) == ['Dont', 'be', 'a']
    def test_ignored_passing_words(self):
        # banned word list
        banned = ['lame', 'loser', 'bogus', 'weirdo', 'bozo']
        speech = ['Everything', 'I', 'say', 'is', 'fine']
        # redact function should return same string
        assert redact(speech, banned) == ['Everything', 'I', 'say', 'is', 'fine']

if __name__ == '__main__':
    unittest.main()