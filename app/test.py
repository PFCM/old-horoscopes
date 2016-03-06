"""Tests for the handlers. It is unlikely these will ever amount to much"""

import unittest

from handlers import APP


class TestMain(unittest.TestCase):
    """Tests that the front page serves correctly"""

    def test_responds(self):
        """Make sure a simple get gives a page back"""
        test_app = APP.test_client()

        response = test_app.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
