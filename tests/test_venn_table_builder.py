import unittest
from src.venn import *
from src.venn_table_builder import *
from src.database_utils import connect

class TestVennTables(unittest.TestCase):
    def test_build_tables(self):
        """Build the tables"""
        rebuild_tables()
        result = exec_get_all('SELECT * FROM users')
        self.assertEqual([], result, "no rows in users")
        result = exec_get_all('SELECT * FROM posts')
        self.assertEqual([], result, "no rows in posts")
        result = exec_get_all('SELECT * FROM passions')
        self.assertEqual([], result, "no rows in passions")
        result = exec_get_all('SELECT * FROM comments')
        self.assertEqual([], result, "no rows in comments")
        result = exec_get_all('SELECT * FROM groups')
        self.assertEqual([], result, "no rows in groups")
        result = exec_get_all('SELECT * FROM usersToPassions')
        self.assertEqual([], result, "no rows in usersToPassions")

    def test_rebuild_tables_is_idempotent(self):
        """Drop and rebuild the tables twice"""
        rebuild_tables()
        rebuild_tables()
        result = exec_get_all('SELECT * FROM users')
        self.assertEqual([], result, "no rows in users")
        result = exec_get_all('SELECT * FROM posts')
        self.assertEqual([], result, "no rows in posts")
        result = exec_get_all('SELECT * FROM passions')
        self.assertEqual([], result, "no rows in passions")
        result = exec_get_all('SELECT * FROM comments')
        self.assertEqual([], result, "no rows in comments")
        result = exec_get_all('SELECT * FROM groups')
        self.assertEqual([], result, "no rows in groups")
        result = exec_get_all('SELECT * FROM usersToPassions')
        self.assertEqual([], result, "no rows in usersToPassions")