import requests
import json


def get_my_token(email, pw) :
    data = {'email': email, 'password':pw}
    response = requests.post("http://13.125.208.1:3000/auth/login", data=data)
    response = json.loads(response.text)
    return(response['token'])

def post_request(url, data) :
    print(url)
    print(data)
    response = requests.post(url, data=data)
    return response.status_code