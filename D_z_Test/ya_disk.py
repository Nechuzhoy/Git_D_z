import os
import requests
from dotenv import load_dotenv
import Status_Http
load_dotenv()
cod = Status_Http.Status_Cod()
class YandexDisk:

    def __init__(self,folder_name,ya_token):
        self.ya_token = ya_token
        self.folder_name = folder_name

    # def get_headers(self):
    #     return {
    #         'Content-Type': 'application/json',
    #         'Authorization': 'OAuth {}'.format(self.ya_token)
    #     }

    def create_dir(self):
        dir = self.folder_name
        URL = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.ya_token)
        }
        response = requests.put(f'{URL}?path={dir}', headers=headers)
        print(f'Создание папки на Яндекс Диске: {cod.server_cod(response)}')
        return response.status_code


if __name__ == '__main__':
    a = YandexDisk('pphjfhpp', 'y0_AgAAAAA0tjMZAADLWwAAAADjKEf9JirHJ2Z_SAKFrQC3ITKKKg5iI7Y')
    a.create_dir()