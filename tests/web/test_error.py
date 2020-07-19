"""
TODO: Doku
"""
from tests import unittest
from tests.web.test_login import TestLogin
from tests.web.utils import (prepare_client, prepare_configuration,
                             restore_configuration)


class TestError(unittest.TestCase):
    """
    TODO: Doku
    """

    def setUp(self) -> None:
        prepare_configuration()
        self.client = prepare_client()
        self.login = TestLogin()

    def tearDown(self) -> None:
        restore_configuration()

    def test_non_existent_logged_out(self) -> None:
        """
        TODO: Doku
        """
        response = self.client.get('/nonexistent')
        self.assertIn(b"Please log in", response.data)

    def test_non_existent_logged_in(self) -> None:
        """
        TODO: Doku
        """
        self.login.log_in(self.client)
        response = self.client.get('/nonexistent')
        self.assertIn(b"404", response.data)
