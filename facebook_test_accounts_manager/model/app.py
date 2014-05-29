from model.request import get, post
from model.test_user import TestUser
import requests


class UserCreationError(StandardError):
    pass


class App:
    MAX_TEST_USERS = 2000   # Current Facebook limitation

    def __init__(self, app_id, token):
        self.id = app_id
        self.token = token

    def _test_users_url(self, parameters):
        return '/%s/accounts/test-users?%s&access_token=%s' % (self.id, parameters, self.token)

    def create_test_user(self):
        result = post(self._test_users_url('installed=true'))
        if result.status_code != requests.codes.ok:
            raise UserCreationError(result.text)

        user_json = result.json()
        return TestUser.from_json(user_json)
