from itertools import cycle


class Solution:
    def __init__(self, key, cypher_text):
        self.__key = key
        self.__decrypted_integers = [a ^ b for a, b in zip(cycle(key), cypher_text)]

    @staticmethod
    def __is_letter(letter):
        return (ord('a') <= letter <= ord('z')) or (ord('A') <= letter <= ord('Z'))

    def get_key(self):
        return ','.join(map(str, self.__key))

    def get_letter_count(self):
        return sum(1 for letter in self.__decrypted_integers if self.__is_letter(letter))

    def get_text(self):
        return ''.join(map(chr, self.__decrypted_integers))

    def get_ascii_sum_of_text(self):
        return sum(self.__decrypted_integers)