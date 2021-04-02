from repos import api
from repos.exceptions import GithubExceptions

import unittest


class TestCreateQuery(unittest.TestCase):
    """Testing the query method"""

    def test_create_query(self):
        languages = ['Ruby', 'Python', 'Java']
        test_min_stars = 10000
        result = api.create_query(languages, test_min_stars)
        self.assertEqual(result, "language: Ruby language: Python language: Java stars:>10000")


class TestGithubApiException(unittest.TestCase):
    """"""
    def test_exception_403(self):
        status_code = 403
        exceptions = GithubExceptions(status_code)
        self.assertTrue("Rate limit" in str(exceptions), "'Rate limit' not found")

    def test_exception_500(self):
        status_code = 500
        exceptions = GithubExceptions(status_code)
        self.assertTrue("status code was" in str(exceptions))


if __name__ == "__main__":
    unittest.main()
