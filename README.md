# COVID-Data-Engineering

## This project is a data engineering pipeline that fetches and stores data from a public COVID data API. The pipeline is written in Python and automates the process of fetching and processing COVID data.

# How to Use
## Run the main.py file in the src folder

# API
## This project used the public API: https://rapidapi.com/api-sports/api/covid-193/

# API key
## The API key was stored as an environment variable using the win10 terminal with: setx RAPID_API_KEY "key_name"

# Features
## - Fetches COVID data from a public API
## - Saves raw json files from API call into a json dump folder
## - Inserts all data in a json file into a database
  
# Requirements
## requests==2.31.0
## sqlite3==3.32.3
## pandas==2.1.1
