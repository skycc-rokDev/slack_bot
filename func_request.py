import requests

def post_request(url, data) :
	print(url)
	print(data)
	response = requests.post(url, data=data)
	return response.status_code