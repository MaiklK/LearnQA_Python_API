import requests

payload = {"name": "Raids"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
print(response.text)
