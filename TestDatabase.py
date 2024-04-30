import unittest
from Database import Database

class TestDatabase(unittest.TestCase):
    def test_login_validation(self):
        # Initialize the database
        db = Database()

        # Test valid login credentials
        valid_email = "zdechazal@gmail.com"
        valid_password = "testpw"
        self.assertTrue(db.login_validation(valid_email, valid_password))

        # Test invalid login credentials
        invalid_email = "invalid@example.com"
        invalid_password = "invalidpassword"
        self.assertFalse(db.login_validation(invalid_email, invalid_password))


