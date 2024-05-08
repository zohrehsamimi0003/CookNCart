import unittest
from unittest.mock import MagicMock
from database import Database
import mysql.connector

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = Database()

    def tearDown(self):
        self.db.conn.close()

    def test_login_validation_success(self):
        # Mocking the cursor and its execute method to return a sample user
        cursor_mock = MagicMock()
        cursor_mock.fetchone.return_value = ('TestUser', 'password123', 'test@example.com', 'Vegetarian')
        self.db.conn.cursor = MagicMock(return_value=cursor_mock)

        # Testing with valid email and password
        result = self.db.login_validation('test@example.com', 'password123')
        self.assertIsNotNone(result)
        self.assertEqual(result, ('TestUser', 'password123', 'test@example.com', 'Vegetarian'))

    def test_login_validation_failure(self):
        # Mocking the cursor and its execute method to raise an error
        cursor_mock = MagicMock()
        cursor_mock.execute.side_effect = mysql.connector.Error()
        self.db.conn.cursor = MagicMock(return_value=cursor_mock)

        # Testing with invalid email and password
        result = self.db.login_validation('invalid@example.com', 'invalid_password')
        self.assertFalse(result)

    def test_check_if_user_exists_success(self):
        # Mocking the cursor and its execute method to return a sample user
        cursor_mock = MagicMock()
        cursor_mock.fetchone.return_value = ('TestUser', 'password123', 'test@example.com', 'Vegetarian')
        self.db.conn.cursor = MagicMock(return_value=cursor_mock)

        # Testing with an existing email
        result = self.db.check_if_user_exists('test@example.com')
        self.assertIsNotNone(result)
        self.assertEqual(result, ('TestUser', 'password123', 'test@example.com', 'Vegetarian'))

    def test_check_if_user_exists_failure(self):
        # Mocking the cursor and its execute method to raise an error
        cursor_mock = MagicMock()
        cursor_mock.execute.side_effect = mysql.connector.Error()
        self.db.conn.cursor = MagicMock(return_value=cursor_mock)

        # Testing with a non-existing email
        result = self.db.check_if_user_exists('nonexistent@example.com')
        self.assertIsNone(result)