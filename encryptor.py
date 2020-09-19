"""
Copyright (C) 2020 Eric Chazan - All Rights Reserved.

You are hereby authorized in sharing this with anyone interested in hiring Eric Chazan.
Thank you for your time :)
"""

from hashlib import sha256

# disclaimer, this is actually more of an obfuscator, but its fine, because there is no decryption requirement.
# we could have used AES if there were a bi-directional encryption requirement
class Encryptor:
    # constructor
    def __init__(self, word):
        ''' Requirement: encrypt a word'''
        self._value = sha256(word.encode('utf-8')).hexdigest()

    # override toString() equivalent
    def __str__(self):
        # truncate to 16 characters for readability.  Note this is also used in the real algorithm.
        # its more than just a toString().
        return str(self._value)[:16]
