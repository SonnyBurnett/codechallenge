from itertools import cycle


class Solution:
    def __init__(self, key, cypher_text):
        self.key = key
        self.decrypted_integers = [a ^ b for a, b in zip(cycle(key), cypher_text)]

    def __is_letter(self, letter):
        return (ord('a') <= letter <= ord('z')) or (ord('A') <= letter <= ord('Z'))

    def get_key(self):
        return ','.join(map(str, self.key))

    def get_letter_count(self):
        return sum(1 for letter in self.decrypted_integers if self.__is_letter(letter))

    def get_text(self):
        return ''.join(map(chr, self.decrypted_integers))

    def get_asci_value(self):
        return sum(self.decrypted_integers)