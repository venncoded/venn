import unittest
from src.venn_command_line import *
from src.venn_table_builder import *
from src.database_utils import connect
from tests.setup import *

class TestTestData(unittest.TestCase):
    def test_insert_users(self):
        """Tests the insertion of user data into database."""
        start_with_test_data()
        result = exec_get_all('SELECT * FROM users')
        self.assertEqual(6, len(result), "three users should be in the database")
    
    def test_insert_passions(self):
        """Tests the insertion of passion data into database."""
        start_with_test_data()
        result = exec_get_all('SELECT * FROM passions')
        self.assertEqual(4, len(result), "four passions should be in the database")

    def test_insert_user_to_passions(self):
        """Tests the insertion of user-passion relationship data into database."""
        start_with_test_data()
        result = exec_get_all('SELECT * FROM usersToPassions')
        self.assertEqual(7, len(result), "seven relationships should be in the database")

    def test_insert_posts(self):
        """Tests the insertion of post data into database."""
        start_with_test_data()
        result = exec_get_all('SELECT * FROM posts')
        self.assertEqual(5, len(result), "five posts should be in the database")

    def test_insert_groups(self):
        """Tests the insertion of user-passion relationship data into database."""
        start_with_test_data()
        result = exec_get_all('SELECT * FROM groups')
        self.assertEqual(2, len(result), "two groups should be in the database")

    def test_insert_comments(self):
        """Tests the insertion of user-passion relationship data into database."""
        start_with_test_data()
        result = exec_get_all('SELECT * FROM comments')
        self.assertEqual(2, len(result), "two comments should be in the database")