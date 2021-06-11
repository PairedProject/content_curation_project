import requests


# Define request headers for api call
headers = {
	'Content-type' : 'Application/json',
	'Authorization' : 'Token 142f7a3ca629dc41d29be36e8e6751594e5dc57b'
}

def get_data(ticker):
	url = f'https://api.tiingo.com/tiingo/daily/{ticker}'
	response = requests.get(url, headers=headers)
	# Uncomment below to see data json object in terminal.
	# print(response.json())
	return response.json()