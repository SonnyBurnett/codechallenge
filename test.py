import pytest
import euler59
import unittest


def test_encryption():
    txt = 'hello'
    key = 'abc'
    bm = encrypt(txt, key)
    msg = decrypt(bm, key)
    assert msg is txt


if __name__ == '__main__':
    unittest.main()