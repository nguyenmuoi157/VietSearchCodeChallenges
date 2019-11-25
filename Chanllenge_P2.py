import unittest
from Challenge_P1 import string_normalize


class Test_VietSearchCodeChallenges_P1(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_string_normalize_test1(self):
        test_case_input = "I like   to      Program   in Python Language. Don’t you?"
        test_case_output = "don i language like program python t you"
        self.assertEqual(string_normalize(test_case_input), test_case_output)

    def test_string_normalize_test2(self):
        test_case_input = "!@#$ %^3 &4* :\<>? cvthe the kc on   |~ rlkre klrjel a   to`"
        test_case_output = "3 4 cvthe kc klrjel rlkre"
        self.assertEqual(string_normalize(test_case_input), test_case_output)


if __name__ == '__main__':
    unittest.main()
