import unittest
from src.venn import *
from src.venn_table_builder import *
from src.database_utils import connect
from tests.setup import *

class TestTestData(unittest.TestCase):
    def test_insert_users(self):
        """Tests the insertion of data into database for testing purposes."""
        start_with_test_data()
        result = exec_get_all('SELECT * FROM users')
        self.assertEqual(3, len(result), "three users should be in the database")
    
    def test_insert_passions(self):
        """Tests the insertion of data into database for testing purposes."""
        start_with_test_data()
        result = exec_get_all('SELECT * FROM passions')
        self.assertEqual(4, len(result), "four passions should be in the database")