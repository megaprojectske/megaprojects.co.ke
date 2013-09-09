"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django import test


class SimpleTest(test.TestCase):

    def test_list(self):
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, 200)
