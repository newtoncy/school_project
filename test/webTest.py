import unittest
from web import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        app.run()


if __name__ == '__main__':
    unittest.main()
