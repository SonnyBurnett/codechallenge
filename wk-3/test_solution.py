import solution


def test_read_csv_cipher():
    assert solution.read_csv_cipher('test_input.txt') == [36, 22, 80, 0, 0, 4]


def test_freq_analysis():
    assert solution.freq([]) == {}

    assert solution.freq([0]) == {0: 1}
    assert solution.freq([0, 0, 0]) == {0: 3}

    assert solution.freq([0, 3, 7]) == {0: 1, 3: 1, 7: 1}
    assert solution.freq([0, 7, 7, 3, 3, 3, 0, 3, 7, 0]) == {0: 3, 3: 4, 7: 3}


def test_cyclic_slice():
    keyLength = 3
    chars = [1, 2, 3, 4, 5]

    assert solution.cyclic_slice(chars, keyLength) == [[1, 4], [2, 5], [3]]


def test_find_encoded_space_char():
    # in this cipher, 3 occurs most often so that must be the space character
    cipher_slice = [3, 3, 3, 7, 7]
    assert solution.find_encoded_space_char(cipher_slice) == 3


def test_how_char_representation_works():
    assert ord(' ') == 32
    assert ord('A') == 65
    assert ord('*') == 42
    assert ord('k') == 107

    assert chr(107) == 'k'


def test_how_XOR_works_for_decimal_ASCII_encoding():
    # XOR as explained in the exercise
    assert 65 ^ 42 == 107
    assert 107 ^ 42 == 65
    # and a property of XOR that is not explained, but verified here:
    assert 65 ^ 107 == 42
    # ... leads to that if we know the encode space characters we can crack the password


def test_crack_key___and_test_decryption():

    text_str = """Th  e    r e      a r e   man y   sp a ces   in  thi s    t e xt,
    s o   we    c a  n    us e     it    e ve n   tho ugh  it  is   sho rt"""

    key_str = "secret"
    key = []
    for c in key_str:
        key.append(ord(c))

    cipher = []
    text = []
    for i, c in enumerate(text_str):
        text.append(ord(c))
        cipher.append(ord(c) ^ key[i % len(key)])

    assert solution.crack_key(cipher, 6) == key

    # now test decryption
    assert solution.decrypt(cipher, key) == text
