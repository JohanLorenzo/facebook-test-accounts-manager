import requests


_BASE_URL = 'https://graph.facebook.com'


def get(end_url):
    return requests.get(_BASE_URL + end_url)


def post(end_url):
    return requests.post(_BASE_URL + end_url)
