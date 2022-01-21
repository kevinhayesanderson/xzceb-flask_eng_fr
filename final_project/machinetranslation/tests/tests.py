from machinetranslation.translator import english_to_french, french_to_english
import unittest
import sys
sys.path.append('/.../xzceb-flask_eng_fr/final_project/machinetranslation')


class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(None), '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(None), '')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')


unittest.main()
