from main import SentenceEncryptor
from parse_errors import WordException, NotAlphaSpace

'''
Requirement:
Must contain unit tests so we know the cases you covered.
'''

def test_non_alphaspace():
    try:
        SentenceEncryptor().encrypt_sentence('I love exclamantion marks!')
    except NotAlphaSpace:
        return
    raise Exception("expected WordException exception")

# keeping a few hard coded values in the tests will protect you from accidental changes in the encryoption algorithm.
def test_single_character():
    result = SentenceEncryptor().encrypt_sentence('S')
    assert result == '3096909d2dd78f63'

def test_blank():
    try:
        SentenceEncryptor().encrypt_sentence('')
    except WordException:
        return
    raise Exception("expected WordException exception")

def test_too_long_sentence():
    try:
        SentenceEncryptor().encrypt_sentence("I really like to go off making long and drawn out sentences")
    except WordException:
        return 
    raise Exception("that guy talked too much, you should have thrown an error")

def test_regular_sentence():
    result = SentenceEncryptor().encrypt_sentence("this is like a really normal sentence")
    assert result == '7a4322e6c10c4c78'

def test_multiple_spaces():
    result1 = SentenceEncryptor().encrypt_sentence("this sentence has    weird spacing")
    result2 = SentenceEncryptor().encrypt_sentence("this    sentence has weird spacing")

    # this was kinda important to me, but it wasn't an explicit requirement:
    assert result1 == result2
