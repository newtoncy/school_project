import unittest

from web.api.keyword import keyword
from web.api.station import station
from web.api.speciality import speciality
from web.api.page import page
from web import app


class MyTestCase(unittest.TestCase):
    def test_station(self):
        with app.test_request_context('/api/station/10'):
            print(station(_id=10))

    def test_speciality(self):
        with app.test_request_context('/api/speciality/132'):
            print(speciality(_id=132))

    def test_page(self):
        with app.test_request_context('/api/page/404'):
            print(page(_id=404))

    def test_keyword(self):
        with app.test_request_context('/api/keyword/56'):
            print(keyword(_id=56))




if __name__ == '__main__':
    unittest.main()
