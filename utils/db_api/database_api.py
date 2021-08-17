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

    def get_dictributions(self):
        url = self.base_url + 'dictribution/'
        params = {
            'format': 'json'
        }
        return requests.get(url, params).json()

    def send_activity(self, activity_type, element_unique_id):
        params = {
            'activity_type': activity_type,
            'element_unique_id': element_unique_id,
            'format': 'json'
        }
        url = self.base_url + 'activity/'
        return requests.post(url, params)

    def get_users(self):
        # TODO return list from local machine
        yield '709379303'
