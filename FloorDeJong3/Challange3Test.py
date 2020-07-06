import unittest

import Challenge3


class TestChallenge3(unittest.TestCase):

    def test_isEnglish(self):
        text = "This iweublkzuxcnzhd;g is 12 a small test to check how many words common words are found from the 100."
        text_jibberish = "djhfiyuvdfiu oiewxMLHUmmn P09WE 8723YRGIaksfibcytdhseta9."
        self.assertEqual(Challenge3.is_english(text), 9)
        self.assertEqual(Challenge3.is_english(text_jibberish), 0)

    def test_isEnglish1(self):
        text = "This iweublkzuxcnzhd;g is 12 a small test to check how many words common words are found from the 100."
        text_jibberish = "djhfiyuvdfiu oiewxMLHUmmn P09WE 8723YRGIaksfibcytdhseta9."

        self.assertEqual(Challenge3.is_english1(text, "en"), 18)
        self.assertEqual(Challenge3.is_english1(text_jibberish, "en"), 0)
