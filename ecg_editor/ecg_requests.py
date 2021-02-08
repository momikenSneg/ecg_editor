import requests
import json

url = '<Ваш API URL>/message?token=<Ваш токен>'


def get_report(data):
    json_data = y = json.dumps(data)
    requests.get(url)


def save_report(data):
    json_data = y = json.dumps(data)