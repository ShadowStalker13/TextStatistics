import unittest
from scr.main import get_words
from scr.main import count_words
from scr.main import count_unique_words
from scr.main import all_words


class TextStatisticsTests(unittest.TestCase):

    def test_cw(self):
        self.assertEqual(type(count_words(r"C:\Users\Home_PC\PycharmProjects\pythonProject1\tests\TextForTests\TestText.txt")), int)

    def test_cuw(self):
        self.assertEqual(type(count_unique_words(r"C:\Users\Home_PC\PycharmProjects\pythonProject1\tests\TextForTests\TestText.txt")), int)

    def test_aw(self):
        self.assertEqual(type(all_words(r"C:\Users\Home_PC\PycharmProjects\pythonProject1\tests\TextForTests\TestText.txt")), dict)

    def test_gw(self):
        self.assertEqual(type(get_words(r"C:\Users\Home_PC\PycharmProjects\pythonProject1\tests\TextForTests\TestText.txt")), list)
