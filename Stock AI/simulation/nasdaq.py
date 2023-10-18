import nasdaqdatalink as nq
import requests


API_KEY = "PdJ5XyKxE9o6iUeSsNgS"

NASDAQ_DATA_LINK_API_KEY = API_KEY



# print(nq.get("EIA/PET_RWTC_D", returns="numpy")[0])


url = "https://data.nasdaq.com/api/v1/datasets/AAPL/chart/1m"
params = {"start": "2023-05-01", "end": "2023-05-02"}
response = print(requests.get(url, params=params))
