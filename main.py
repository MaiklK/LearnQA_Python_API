import requests
import json

payload = {"name": "Raids"}
key = 'answer'

response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
response = json.loads(response.text)

if key in response:
    print(response[key])
else:
    print(f"Ключа {key} в JSON нет")
