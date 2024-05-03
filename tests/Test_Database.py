import unittest
from unittest.mock import patch, MagicMock
from Database import Database  # Import your Database class

class Test_Database(unittest.TestCase):

    @patch('Database.mysql.connector.connect')
    def test_login_validation_valid(self, mock_connect):
        # Mocking database connection
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = {'id': 1, 'username': 'test_user'}
        mock_connect.return_value.cursor.return_value = mock_cursor

        # Initialize your Database object
        db = Database()

        # Test for valid login credentials
        user = db.login_validation("valid_email@example.com", "valid_password")
        self.assertIsNotNone(user)  # Assert that the user exists

    @patch('Database.mysql.connector.connect')
    def test_login_validation_invalid(self, mock_connect):
        # Mocking database connection
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = None  # Simulate no user found
        mock_connect.return_value.cursor.return_value = mock_cursor

        # Initialize your Database object
        db = Database()

        # Test for invalid login credentials
        user = db.login_validation("invalid_email@example.com", "invalid_password")
        self.assertIsNone(user)  # Assert that no user is returned

    @patch('Database.mysql.connector.connect')
    def test_insert_user_success(self, mock_connect):
        # Mocking database connection
        mock_cursor = MagicMock()
        mock_cursor.rowcount = 1  # Simulate successful insertion
        mock_connect.return_value.cursor.return_value = mock_cursor

        # Initialize your Database object
        db = Database()

        # Test for successful insertion
        result = db.insert_user("test_username", "test_email@example.com", "test_password", "Vegetarian")
        self.assertEqual(result, 1)  # Assert that rowcount is 1 indicating successful insertion

    @patch('Database.mysql.connector.connect')
    def test_insert_user_failure(self, mock_connect):
        # Mocking database connection
        mock_cursor = MagicMock()
        mock_cursor.rowcount = 0  # Simulate failed insertion
        mock_connect.return_value.cursor.return_value = mock_cursor

        # Initialize your Database object
        db = Database()

        # Test for failed insertion
        result = db.insert_user("test_username", "test_email@example.com", "test_password", "Vegetarian")
        self.assertEqual(result, 0)  # Assert that rowcount is 0 indicating failed insertion

    @patch('Database.mysql.connector.connect')
    def test_delete_user(self, mock_connect):
        # Mocking database connection
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor

        # Initialize your Database object
        db = Database()

        # Test delete user
        user = MagicMock(email="test_email@example.com")
        db.delete_user(user)
        mock_cursor.execute.assert_called_once_with('''DELETE FROM users WHERE Email = %s;''', ("test_email@example.com",))

    @patch('Database.mysql.connector.connect')
    def test_update_password(self, mock_connect):
        # Mocking database connection
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor

        # Initialize your Database object
        db = Database()

        # Test update password
        user = MagicMock(email="test_email@example.com")
        db.update_password(user, "new_password")
        mock_cursor.execute.assert_called_once_with('''UPDATE users SET UserPassword = %s WHERE Email = %s;''', ("new_password", "test_email@example.com"))

    @patch('Database.mysql.connector.connect')
    def test_update_diet_type(self, mock_connect):
        # Mocking database connection
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor

        # Initialize your Database object
        db = Database()

        # Test update diet type
        user = MagicMock(email="test_email@example.com")
        db.update_diet_type(user, "new_diet_type")
        mock_cursor.execute.assert_called_once_with('''SELECT DietTypeId INTO @DietTypeId FROM diet_types WHERE DietType = %s;
            UPDATE users SET DietTypeId = @DietTypeId WHERE Email = %s;''', ("new_diet_type", "test_email@example.com"))
