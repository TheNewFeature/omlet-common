import unittest

from omlet_common.regex import validate_email


class RegexEmailTestCase(unittest.TestCase):

    def test_regex_email(self):
        email = 'username123@domain.com'
        self.assertTrue(validate_email(email))

        email = 'user.name@domain.com'
        self.assertTrue(validate_email(email))

        email = 'user0_name1@domain.com'
        self.assertTrue(validate_email(email))

        non_email = 'username'
        self.assertFalse(validate_email(non_email))


if __name__ == "__main__":
    unittest.main()
