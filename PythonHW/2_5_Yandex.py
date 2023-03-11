import requests
import os

class YaDisk:

    def __init__(self, token: str):
        self.token = token
        self.yandex_url = 'https://cloud-api.yandex.net/'

    def _get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
    
    def _get_upload_link(self, disk_file_path):
        upload_url = self.yandex_url + 'v1/disk/resources/upload'
        headers = self._get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(url=upload_url, headers=headers, params=params)
        return response.json()

    def get_files_list(self):
        files_url = self.yandex_url + 'v1/disk/resources/files'
        headers = self._get_headers()
        response = requests.get(url=files_url, headers=headers)
        return response.json()

    def upload_file(self, file_dest_path, file_source_path):
        href_response = self._get_upload_link(file_dest_path)
        href = href_response.get('href', '')
        with open(file_source_path, 'rb') as file:
            response = requests.put(url=href, data=file)
            response.raise_for_status()
            return response.status_code           


if __name__ == '__main__':
    # get a file path and a token 
    current = os.getcwd()
    folder_name = 'PythonHW'
    file_name = '2_5_Super_Hero.py'
    path_to_file = os.path.join(current, folder_name, file_name)
    token = ''

    # upload the file to yandex disk
    ya = YaDisk(token)
    print('\nFile source path: ' + path_to_file)
    status_code = ya.upload_file('example.py', path_to_file)
    if status_code == 201:
        print('Success: file loaded to yandex disk')
    else:
        print(f'Error: code: {status_code}')