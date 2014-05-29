from model.request import post
import requests


class FriendshipError(StandardError):
    pass


class TestUser:
    def __init__(self, in_app_id, token):
        self.id = in_app_id
        self.token = token

    def make_friend_request(self, other_user):
        result = post('/%s/friends/%s?&access_token=%s' % (self.id, other_user.id, self.token))
        if result.status_code != requests.codes.ok:
            raise FriendshipError(result.text)

    def make_friend(self, other_user):
        other_user.make_friend_request(self)
        self.make_friend_request(other_user)

    @classmethod
    def from_json(cls, user_json):
        return TestUser(user_json['id'], user_json['access_token'])
