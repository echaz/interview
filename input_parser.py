from parse_errors import WordException, NotAlphaSpace

"""
Copyright (C) 2020 Eric Chazan - All Rights Reserved. 

You are hereby authorized in sharing this with anyone interested in hiring Eric Chazan.
Thank you for your time :)
"""

class InputParser():
    """
    Requirement: Take in a sentence… no longer than 7 words and only alphabets and space. No punctuations.
    """

    # class variables
    MAX_WORDS = 7

    def parse(self, input_string):
        self.input_string = input_string
        self._validate_alpha_space()
        return self._find_words()

    # methods that start with an underscore in python are considered private.  But in python,
    # "we're all consenting adults here", and it's not enforced
    def _find_words(self):
        # split takes in a string, and outputs lists of words segmented by the argument.
        potential_words = self.input_string.split(' ')

        # take the potential words, and find the actual words:
        words = list()
        for word in potential_words:
            if len(word) > 0:
                words.append(word)

        if len(words) > InputParser.MAX_WORDS:
            raise WordException(f"we expected not greater than {InputParser.MAX_WORDS} words, but we counted {len(words)} ")

        if len(words) == 0:
            raise WordException('we found no words.')

        return words

    def _validate_alpha_space(self):
        # ord returns the integer value for the string
        for c in self.input_string:
            if c != ' ' and c.isalpha() ==False:
                raise NotAlphaSpace(f"character {c} in position {self.input_string.find(c)} is not a space or alphabetical.")
