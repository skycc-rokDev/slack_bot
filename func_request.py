import requests

def post_request(url, data) :
	response = requests.post(url, data=data)
	return response.status_code