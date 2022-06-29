from json.decoder import JSONDecodeError
import requests
import pytest


data = {
    'email': 'vinkotov@exemple.com',
    'password': '1234'
}

url = 'https://playground.learnqa.ru/api/user/login'
responce1 = requests.post(url, data=data)
print(responce1.status_code)
