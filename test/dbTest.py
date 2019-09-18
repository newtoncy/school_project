# 数据库的单元测试
import unittest
import db


class DBTestCase(unittest.TestCase):
    def test_insert(self):
        session = db.Session()
        page = db.table.Pages()
        pass


if __name__ == '__main__':
    unittest.main()
