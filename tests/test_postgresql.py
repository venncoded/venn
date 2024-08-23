import unittest
from src.database_utils import connect

class TestPostgreSQL(unittest.TestCase):

    def test_connect(self):
        conn = connect()
        cur = conn.cursor()
        cur.execute('SELECT VERSION()')
        self.assertTrue(cur.fetchone()[0].startswith('PostgreSQL'))
        conn.close()

if __name__ == '__main__':
    unittest.main()