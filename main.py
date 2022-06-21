from json.decoder import JSONDecodeError
import requests

payload = {"name": "Raids"}
key = 'answer'

response = requests.get("https://playground.learnqa.ru/api/get_text", params=payload)
print(response.text)
try:
    parsed_response_text = response.json()
    print(parsed_response_text)
except JSONDecodeError:
    print("Response in not a JSON format")