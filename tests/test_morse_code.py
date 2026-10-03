import unittest

from MorseCode import morse_to_text, text_to_morse


class MorseCodeTests(unittest.TestCase):
    def test_text_to_morse_encodes_words(self):
        self.assertEqual(text_to_morse("sos help"), "... --- ... / .... . .-.. .--.")

    def test_morse_to_text_decodes_words(self):
        self.assertEqual(morse_to_text("... --- ... / .... . .-.. .--."), "sos help")

    def test_unsupported_characters_are_rejected(self):
        with self.assertRaises(ValueError):
            text_to_morse("hello #")

    def test_unknown_morse_codes_are_visible(self):
        self.assertEqual(morse_to_text("... ....-.-"), "s^")


if __name__ == "__main__":
    unittest.main()
