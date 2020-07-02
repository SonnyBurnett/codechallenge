import unittest

import Challenge3

class TestChallenge3(unittest.TestCase):

    def test_xorDecryptAsciiList(self):
        key = "abc"
        greeting = "hello"

        ascii_greeting = [ord(letter) for letter in greeting]
        encrypted_greeting = xor_decrypt_ascii_list()
