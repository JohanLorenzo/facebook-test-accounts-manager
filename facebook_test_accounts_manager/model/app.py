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

    @property
    def test_users(self):
        all_users_request = get(self._test_users_url('limit=%d' % self.MAX_TEST_USERS))
        returned_json = all_users_request.json()
        users_json = returned_json['data']
        return [TestUser.from_json(user_json) for user_json in users_json]
