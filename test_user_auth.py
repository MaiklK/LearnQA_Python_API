import requests


class TestUserAuth:
    def test_user_auth(self):
        data = {
            'email': 'vinkotov@exemple.com',
            'password': '1234'
        }

        url = 'https://playground.learnqa.ru/api/user/login'
        responce1 = requests.post(url, data=data)

        assert "auth_sid" in responce1.cookies, "There is no auth cookie in the response1"
        assert "x-csrf-token" in responce1.headers, "There in no CSRF token in response1"
        assert "user_id" in responce1.json(), "There is no user id in the response1"

        auth_sid = responce1.cookies.get("auth_sid")
        token = responce1.headers.get("x_csrf_token")
        user_id_from_auth_method = responce1.json()["user_id"]

        url = 'https://playground.learnqa.ru/api/user/auth'
        responce2 = requests.get(url, headers={"x-csrf": token}, cookies={"auth_sid": auth_sid})

        assert "user_id" in responce2.json(), "There is no user id in the response2"
        user_id_from_check_method = responce2.json("user_id")

        assert user_id_from_auth_method == user_id_from_check_method, "User id from auth method is not equal to user " \
                                                                      "from check method"


data = {
    'email': 'vinkotov@exemple.com',
    'password': '1234'
}

url = 'https://playground.learnqa.ru/api/user/login'
responce1 = requests.post(url, data=data)
print(responce1.status_code)
