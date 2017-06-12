from django.test import TestCase

# Create your tests here.
from challenge.views import validate_text


class ChallengeTests(TestCase):

    def test_input_a_equal_output_a(self):
        input = "a"
        text = "a"
        output = validate_text(input, text)
        self.assertEqual(output, input)

    def test_input_ab_equal_output_ab(self):
        input = "ab"
        text = "ab"
        output = validate_text(input, text)
        self.assertEqual(output, "ab")

    def test_input_abcd_equal_output_abcd(self):
        input = "abcd"
        text = "abcdefghijk"
        output = validate_text(input, text)
        self.assertEqual(output, "abcd")

    def test_input_wrong_letter_but_contains_letter(self):
        input = "abbddff"
        text = "abcdefghijk"
        output = validate_text(input, text)
        self.assertEqual(output, "ab-d-f-")

    def test_input_wrong_letter_no_contains_letter(self):
        input = "lmn"
        text = "abcdefghijk"
        output = validate_text(input, text)
        self.assertEqual(output, "***")

    def test_input_bigger_than_text(self):
        input = "abcdefghijklmn"
        text = "abcdefghijk"
        output = validate_text(input, text)
        self.assertEqual(output, text)

    def test_input_uppercase_found(self):
        input = "B"
        text = "Bill Gates"
        output = validate_text(input, text)
        self.assertEqual(output, input)

    def test_input_lowercase_not_found(self):
        input = "b"
        text = "Bill Gates"
        output = validate_text(input, text)
        self.assertEqual(output, "*")

    def test_input_part_text(self):
        input = "It is fine"
        text = "It is fine to celebrate success but it is more important to heed the lessons of failure. By Bill Gates"
        output = validate_text(input, text)
        self.assertEqual(output, input)
