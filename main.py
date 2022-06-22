from json.decoder import JSONDecodeError
import requests

payload = {"name": "Raids"}
key = 'answer'

response = requests.post("https://playground.learnqa.ru/api/check_type", data=payload)
print(response.text)
try:
    parsed_response_text = response.json()
    print(parsed_response_text)
except JSONDecodeError:
    print("Response in not a JSON format")
