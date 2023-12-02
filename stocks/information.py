import requests 

from django.conf import settings

API_KEY = settings.API_KEY

headers = {
	'Content-Type': 'application/json',
	'Authorization': f'Token {API_KEY}'
}

def get_search_data(stock_name):
	url = f'https://api.tiingo.com/tiingo/utilities/search?query={stock_name}'
	response = requests.get(url, headers=headers)
	data = response.json()
	return data 

def get_price_information(stock_code):
	url = f'https://api.tiingo.com/tiingo/daily/{stock_code}/prices'
	response = requests.get(url, headers=headers)
	data = response.json()
	return data 

def get_meta_data(stock_code):
	url = f'https://api.tiingo.com/tiingo/daily/{stock_code}'
	response = requests.get(url, headers=headers)
	data = response.json()
	return data

def list_of_crypto_data():
	url = 'https://api.tiingo.com/tiingo/crypto' 
	response = requests.get(url, headers=headers)
	data = response.json()
	return data 

def get_stocks_fundementals():
	url = 'https://api.tiingo.com/tiingo/fundamentals/definitions'
	response = requests.get(url, headers=headers)
	data = response.json()
	return data