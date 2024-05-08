'''
import unittest
from unittest.mock import patch, MagicMock
from database import Database  # Import your Database class

class TestDatabase(unittest.TestCase):

    @patch('Database.mysql.connector.connect')
    def test_login_validation_valid(self, mock_connect):
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = {'UserName': 'test_user'}
        mock_connect.return_value.cursor.return_value = mock_cursor
        db = Database()
        user = db.login_validation("valid_email@example.com", "valid_password")
        self.assertIsNotNone(user)

    @patch('Database.mysql.connector.connect')
    def test_login_validation_invalid(self, mock_connect):
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = None
        mock_connect.return_value.cursor.return_value = mock_cursor
        db = Database()
        user = db.login_validation("invalid_email@example.com", "invalid_password")
        self.assertIsNone(user)

    @patch('Database.mysql.connector.connect')
    def test_insert_user_success(self, mock_connect):
        mock_cursor = MagicMock()
        mock_cursor.rowcount = 1
        mock_connect.return_value.cursor.return_value = mock_cursor
        db = Database()
        result = db.insert_user("test_username", "test_email@example.com", "test_password", "Vegetarian")
        self.assertEqual(result, 1)

    @patch('Database.mysql.connector.connect')
    def test_insert_user_failure(self, mock_connect):
        mock_cursor = MagicMock()
        mock_cursor.rowcount = 0
        mock_connect.return_value.cursor.return_value = mock_cursor
        db = Database()
        result = db.insert_user("test_username", "test_email@example.com", "test_password", "Vegetarian")
        self.assertEqual(result, 0)

    @patch('Database.mysql.connector.connect')
    def test_delete_user(self, mock_connect):
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        db = Database()
        user = MagicMock(email="test_email@example.com")
        db.delete_user(user)
        mock_cursor.execute.assert_called_once_with('''DELETE FROM users WHERE Email = %s;''', ("test_email@example.com",))

    @patch('Database.mysql.connector.connect')
    def test_update_password(self, mock_connect):
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        db = Database()
        user = MagicMock(email="test_email@example.com")
        db.update_password(user, "new_password")
        mock_cursor.execute.assert_called_once_with('''UPDATE users SET UserPassword = %s WHERE Email = %s;''', ("new_password", "test_email@example.com"))

    @patch('Database.mysql.connector.connect')
    def test_update_diet_type(self, mock_connect):
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        db = Database()
        user = MagicMock(email="test_email@example.com")
        db.update_diet_type(user, "new_diet_type")
        mock_cursor.execute.assert_called_once_with('''SELECT DietTypeId INTO @DietTypeId FROM diet_types WHERE DietType = %s;
            UPDATE users SET DietTypeId = @DietTypeId WHERE Email = %s;''', ("new_diet_type", "test_email@example.com"))

    @patch('Database.mysql.connector.connect')
    def test_get_random_recipes(self, mock_connect):
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = {'RecipeTitle': 'Test Recipe'}
        mock_connect.return_value.cursor.return_value = mock_cursor
        db = Database()
        random_recipe = db.get_random_recipes("Lunch", 3)
        self.assertIsNotNone(random_recipe)

if __name__ == '__main__':
    unittest.main()'''
