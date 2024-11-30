import random
import string

import pytest
import requests


class BaseEndpoint:
    api_key = 'Bot MTI4NjYwOTgxOTEzNzk5ODg4Mw.Gj2Mlk.YsVgU6PYv7xVW5bl7RYt9DLg2QeCU4OXToIiSw'
    channel_id = 1305528788821606481
    base_url = 'https://discord.com/api/v10'

    def __init__(self):
        self.response_json = None
        self.response = None

    def get_request(self, url, headers):
        self.response = requests.get(url, headers=headers, verify=False)
        self.response_json = self.response.json()
        return self.response_json

    def post_request(self, url, headers, data):
        self.response = requests.post(url, headers=headers, data=data, verify=False)
        self.response_json = self.response.json()
        return self.response_json

    def delete_request(self, url, headers):
        self.response = requests.delete(url, headers=headers, verify=False)
        return self.response

    def check_status_code(self, code):
        if self.response.status_code == code:
            pass
        else:
            pytest.fail(f'Error: {self.response.status_code}')

    def make_latin_lower(self, length):
        latin_lowercase_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
        return latin_lowercase_string

    def make_digit(self, length):
        digit_string = ''.join(random.choice(string.digits) for _ in range(length))
        return digit_string
