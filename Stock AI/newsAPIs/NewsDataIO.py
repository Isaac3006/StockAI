# MISSING UNIVERSAL DATES


import datetime
import json

import requests

newsAPIKey = "pub_2439147b28baa2832e2c4e762e702dd89dd0f"




def getNewsQuery():

    today = datetime.datetime.now()

    today = today.strftime('%Y-%m-%d')

    newsQuery = f"""https://newsdata.io/api/1/news?apikey={newsAPIKey}&category=business,politics,technology&country=us&from_date={today}&to_date={today}"""
    
    return newsQuery



# Working

def getNews():


    resp = json.loads(requests.get(getNewsQuery()).text)

    

    res =  [[val['title'], val['pubDate']] for val in resp['results']]

    return res

def getNewsTest():


    resp = json.loads(requests.get(getNewsQuery()).text)

    

    res =  [[val['title'], val['pubDate'], val["creator"], val["link"]] for val in resp['results']]

    return res

