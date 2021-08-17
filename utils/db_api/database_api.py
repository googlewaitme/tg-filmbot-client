import requests
from utils.db.models import User


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
            'format': 'json',
            'to_send': True
        }
        return requests.get(url, params).json()

    def set_dictribution_is_sended(self, params):
        url = params['url']
        params['is_send'] = True
        requests.patch(url, params)

    def send_activity(self, activity_type, element_unique_id):
        params = {
            'activity_type': activity_type,
            'element_unique_id': element_unique_id,
            'format': 'json'
        }
        url = self.base_url + 'activity/'
        return requests.post(url, params)

    def get_or_create(self, telegram_id):
        user, created = User.get_or_create(telegram_id=telegram_id)
        return user, created

    def add_user(self, telegram_id):
        User.create(telegram_id=telegram_id)

    def get_users(self):
        for user in User.select():
            yield user.telegram_id
