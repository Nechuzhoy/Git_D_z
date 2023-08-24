import unittest
import requests
from uniquen_names import create_all_list,create_all_names_list
from top_name import create_all_list, create_all_names_list, list_in_set
from ya_disk import YandexDisk

class TestUniquenNames(unittest.TestCase):
    def test_create_all_list(self):
        x = [
            ["Евгений Шмаргунов"],
            ["Филипп Воронов"],
            ["Олег Булыгин"],
            ["Владимир Чебукин"]
            ]
        res = create_all_list(x)
        expected = ["Евгений Шмаргунов", "Филипп Воронов","Олег Булыгин","Владимир Чебукин"]
        self.assertEqual(res, expected)

    def test_create_all_names_list(self):
        x = ["Евгений Шмаргунов", "Филипп Воронов","Олег Булыгин","Владимир Чебукин"]
        res = create_all_names_list(x)
        expected = ["Евгений", "Филипп","Олег","Владимир"]
        self.assertEqual(res, expected)

    def test_list_in_set(self):
        x = ["Евгений", "Филипп","Олег","Владимир"]
        res = list_in_set(x)
        expected = {'Олег', 'Филипп', 'Евгений', 'Владимир'}
        self.assertEqual(res, expected)


class TestYandexDisk(unittest.TestCase):

        def test_create_dir(self):
            ya = YandexDisk(ya_token='', folder_name='123')
            self.assertEqual(ya.create_dir(), 201)

        def test_create_dir_folder(self):
            ya = YandexDisk(ya_token='', folder_name='321')
            self.assertEqual(ya.create_dir(), 409)


if __name__ == '__main__':
    unittest.main()