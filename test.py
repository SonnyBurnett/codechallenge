
import unittest
import pytest
from euler59 import analysis, encrypt, decrypt


# test the ecryption / decryption routine
def test_encryption():
    txt = 'hello'
    key = 'abc'
    bm = encrypt(txt, key)
    msg = decrypt(bm, key)
    assert msg == txt


# test the analysis routine
def test_analysis():
    txt = "a b  c   d    e     f      g "
    key = 'xyz'
    bm = encrypt(txt, key)
    print(bm)
    guessed_key = analysis(bm)
    assert key == guessed_key


if __name__ == '__main__':
    unittest.main()
