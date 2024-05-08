import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        # Create a sample user
        self.user = User("John Doe", "password123", "john@example.com", "Vegetarian")

    def test_initialization(self):
        # Test initialization of User object
        self.assertEqual(self.user.name, "John Doe")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.email, "john@example.com")
        self.assertEqual(self.user.diet_type, "Vegetarian")

    def test_update_user_data(self):
        # Test updating user data
        self.user.update_user_data("Jane Doe", "newpassword456", "Vegan")
        self.assertEqual(self.user.name, "Jane Doe")
        self.assertEqual(self.user.password, "newpassword456")
        self.assertEqual(self.user.diet_type, "Vegan")