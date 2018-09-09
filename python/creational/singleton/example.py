import logging
import os
import sqlite3
import unittest


FILE_PATH = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = 'example.db'
class Database(object):
    __shared_state = {}
    def __init__(self):
        if not Database.__shared_state:
            logging.basicConfig(level=logging.INFO)
            logging.info('New instance created!')
        else:
            logging.info('State reused!')
        self.__dict__ = self.__shared_state
        self.filename = os.path.join(FILE_PATH, FILE_NAME)
        if not os.path.isfile(self.filename):
            self.createDatabase()
        else:
            self._db = sqlite3.connect(self.filename)
            self._db.row_factory = sqlite3.Row
            self.cursor = self._db.cursor()
    def createDatabase(self):
        logging.info('Creating Database in {}'.format(self.filename))
        self._db = sqlite3.connect(self.filename)
        self._db.row_factory = sqlite3.Row
        self.cursor = self._db.cursor()
        self.cursor.executescript("""
            CREATE TABLE IF NOT EXISTS test_table(
                rowid INTEGER,
                field TEXT
            );
        """)
        self.commit()
    def execute(self, sql, *params):
        return self.cursor.execute(sql, params)
    def fetchone(self):
        return self.cursor.fetchone()
    def fetchall(self):
        return self.cursor.fetchall()
    def lastrowid(self):
        return self.cursor.lastrowid
    def commit(self):
        return self._db.commit()
    def close(self):
        self.commit()
        self._db.close()
        logging.info('Connection closed.')


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database()

    def test_1(self):
        db2 = Database()
        self.assertNotEqual(id(self.db), id(db2))
        self.assertEqual(self.db.cursor, db2.cursor)

    def tearDown(self):
        self.db.close()
        if os.path.isfile(self.db.filename):
            os.remove(self.db.filename)


if __name__ == '__main__':
    unittest.main()
