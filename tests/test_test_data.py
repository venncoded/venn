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
        self.assertEqual(3, len(result), "three users should be in the database")
    
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