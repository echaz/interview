"""
Copyright (C) 2020 Eric Chazan - All Rights Reserved.

You are hereby authorized in sharing this with anyone interested in hiring Eric Chazan.
Thank you for your time :)
"""
import sys

from encryptor import Encryptor
from input_parser import InputParser

class SentenceEncryptor:

    def __init__(self, log_steps=True):
        self.parser = InputParser()
        self.log_steps = log_steps

    def encrypt_words(self, words):
        '''
        Requirement:
        I want to encrypt each word in the sentence.
        '''
        retval = list()
        for word in words:
            retval.append(Encryptor(word))
        return retval


    def encrypt_sentence(self, sentence):
        '''
        encrypt the whole sentence
        '''
        words = InputParser().parse(sentence)

        if self.log_steps:
            print(f'Phrase: {" ".join([word for word in words])}')

        encrypted_words = self.encrypt_words(words)

        if self.log_steps:
            print(f"Encrypted pass 1: {' '.join(str(w) for w in encrypted_words)}")

        return self.distil_sentence(encrypted_words, 2)

    # it's always a little controversial to use recursion in an interview.  I'm going for it.
    def distil_sentence(self, words, step_index):
        '''
        Requirement: Then I want to encrypt again by combining pairs of words.
        I want to keep doing this until there is a single encrypted string that represents the sentence.
        '''
        result = list()

        # loops over pairs:
        for index in range(1, len(words), 2):
            string_to_encrypt = str(words[index - 1]) + ' ' + str(words[index])
            result.append(Encryptor(string_to_encrypt))

        # is the list count odd?  then encrypt the guy at the end:
        if len(words) % 2 == 1:
            result.append(Encryptor(str(words[-1])))  # negative array indexes take from the end of the list.

        print(f"Encrypted pass {step_index}: {' '.join(str(w) for w in result)}")

        if len(result) > 1:
            return self.distil_sentence(result, step_index + 1)

        # return the only word left:
        return str(result[0])


# this is how you do a "main" method like in java.  Yes, it is a little weird.
if __name__ == "__main__":
    commandline_arguments_as_string = ' '.join(sys.argv[1:])
    SentenceEncryptor(True).encrypt_sentence(commandline_arguments_as_string)
