from json.decoder import JSONDecodeError
import requests

payload = {"login": "secret_login",
           "password": "secret_pass"}


response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

print(response.status_code)
print(response.text)
print(dict(response.cookies))
cookie_value = response.cookies

response2 = requests.get("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookie_value)
print(response2.text)
# try:
#     parsed_response_text = response.json()
#     print(parsed_response_text)
# except JSONDecodeError:
#     print("Response in not a JSON format")
