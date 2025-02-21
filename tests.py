"""This file is the unit test for SimpleResume web application.
"""
from users import User
import unittest


class TestUser(unittest.TestCase):
    """Class containing unit test for User object
    """
    def setUp(self):
        """Initialization of user object.
        """
        self.user = User()
        self.user.experiences = [
            {"start_date": "2016-01-01"},
            {"start_date": "2017-01-01"},
            {"start_date": "2018-01-01"},
            {"start_date": "2019-01-01"}
        ]


    def test_sort_user_experience(self):
        """Test function: sort_user_experience
        """
        expected_result = [
            {"start_date": "2019-01-01"},
            {"start_date": "2018-01-01"},
            {"start_date": "2017-01-01"},
            {"start_date": "2016-01-01"}
        ]
        self.user.sort_user_experience()
        self.assertEqual(self.user.experiences, expected_result)


    def test_sort_user_certifications(self):
        """Test function: sort_user_certifications
        """
        self.user.certifications = [
            {"date": "2016-01-01"},
            {"date": "2017-01-01"},
            {"date": "2018-01-01"},
            {"date": "2019-01-01"}
        ]
        expected_result = [
            {"date": "2019-01-01"},
            {"date": "2018-01-01"},
            {"date": "2017-01-01"},
            {"date": "2016-01-01"}
        ]
        self.user.sort_user_certifications()
        self.assertEqual(self.user.certifications, expected_result)


if __name__ == "__main__":
    unittest.main()
