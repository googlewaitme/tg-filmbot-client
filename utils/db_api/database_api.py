import requests


class DBApi():
    def __init__(self, base_url):
        self.base_url = base_url + 'api/'

    def get_films(self, search_request):
        url = self.base_url + 'film/'
        params = {
            'search_data': search_request,
            'format': 'json'
        }
        return requests.get(url, params).json()

    def get_message(self, unique_name):
        url = self.base_url + 'message/'
        params = {
            'unique_name': unique_name,
            'format': 'json'
        }
        return requests.get(url, params).json()[0]['text']
