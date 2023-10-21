import requests
import os

def get_data() -> dict:
    
	"""
	Make an API call to fetch json response data for statistics endpoint.

	Returns:
	data (dict): json response data
	"""

	# get the RapidAPI key from the environment variable
	rapid_api_key = os.getenv("RAPID_API_KEY")

	# set the headers for the API request
	headers = {'X-RapidAPI-Key': rapid_api_key,
				'X-RapidAPI-Host': 'covid-193.p.rapidapi.com'}

	# make the API request
	response = requests.get("https://covid-193.p.rapidapi.com/statistics",headers=headers)
	data = response.json()

	# return response data
	return data

def get_history(
	country:str,
	day:str
) -> dict:

	"""
	Make an API call to fetch json response data for history endpoint.

	Parameters:
	country (str): A country name as defined in the list of countries in the statistic endpoint
	day (str): A date in the form "yyyy-mm-dd"

	Returns:
	data (dict): json response data
	"""

	# get the RapidAPI key from the environment variable
	rapid_api_key = os.getenv("RAPID_API_KEY")

	# set the parameters for the API request
	params = {
	'country': country,
	'day': day
	}
	# set the headers for the API request
	headers = {'X-RapidAPI-Key': rapid_api_key,
				'X-RapidAPI-Host': 'covid-193.p.rapidapi.com'}

	# make the API request
	response = requests.get("https://covid-193.p.rapidapi.com/history",params = params,headers=headers)
	data = response.json()

	# return response data
	return data








