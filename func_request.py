import requests
import json


def get_my_token(email, pw) :
    #try :
    data = {'email': email, 'password':pw}
    response = requests.post("http://13.125.208.1:3000/auth/login", data=data)
    response = json.loads(response.text)
    return(response['token'])
    #except :
    #    return 0

def post_request_token(url, data, token) :
    headers = {'token': token}
    print(url)
    print(data)
    response = requests.post(url, data=data, headers=headers)
    return response.status_code

def post_request_token_get(url, data, token) :
    headers = {'token': token}
    print(url)
    print(data)
    response = requests.post(url, data=data, headers=headers)
    return response.status_code, response.text

def post_request(url, data) :
    print(url)
    print(data)
    response = requests.post(url, data=data)
    return response.status_code