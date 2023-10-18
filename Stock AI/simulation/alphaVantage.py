import requests


API_KEY = ""


url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=1min&apikey={API_KEY}'
r = requests.get(url)
data = r.json()

print([val for val in data['Time Series (1min)']])