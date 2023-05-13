import requests
import json


def get_my_token(email, pw) :
    #try :
    data = {'email': email, 'password':pw}
    response = requests.post("http://13.125.208.1:3000/auth/login", data=data)
    response = json.loads(response.text)
    print(response)
    return(response['token'])
    #except :
    #    return 0

def delete_request_token(url, token) :
    headers = {'token': token}
    print(url)
    print(headers)
    response = requests.delete(url, headers=headers)
    print(response.text)
    return response.status_code

def post_request_token(url, data, token) :
    headers = {'token': token}
    print(url)
    print(data)
    response = requests.post(url, data=data, headers=headers)
    return response.status_code

def get_request_token(url, token) :
    headers = {'token': token}
    response = requests.get(url, headers=headers)
    print("[get_requset_token]" + str(response))
    return response.status_code, response.text

def post_request(url, data) :
    print(url)
    print(data)
    response = requests.post(url, data=data)
    return response.status_code