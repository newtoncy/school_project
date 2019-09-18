import json
import unittest
from WebInfoHandle import WebInfo, updateDB

with open('job(0-400).json', encoding='utf-8') as file:
    foo = json.load(file)


class MyTestCase(unittest.TestCase):
    def test_speciality_station_words(self):
        for i in range(100):
            webInfo = WebInfo().loadDict(foo[str(i)])
            print('专业:' + str(webInfo.speciality))
            print('职位:' + webInfo.station)
            print('词:' + str(webInfo.words))

    def test_dateTime(self):
        for i in range(100):
            webInfo = WebInfo().loadDict(foo[str(i)])
            self.assertTrue(webInfo.dateStr)

    def test_updateDB(self):
        for item in foo.values():
            webInfo = WebInfo().loadDict(item)
            updateDB.updateDB(webInfo)


if __name__ == '__main__':
    unittest.main()
