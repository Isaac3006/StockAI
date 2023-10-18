import requests
import json


# INCONSISTENT



API_KEY = ""


url = f"https://gnews.io/api/v4/search?q=example&lang=en&country=us&max=10&apikey={API_KEY}"


def getNews():


    news = json.loads(requests.get(url).text)["articles"]

    return [[new["title"], new["publishedAt"]] for new in news]


def getNewsTest():


    news = json.loads(requests.get(url).text)["articles"]

    return [[new["title"], new["publishedAt"], new["source"]["url"]] for new in news]



print(getNews())




