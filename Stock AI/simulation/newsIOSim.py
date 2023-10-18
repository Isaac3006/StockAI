# MISSING UNIVERSAL DATES


import datetime
import json

import requests

newsAPIKey = ""




def getNewsQuery(date):



    newsQuery = f"""https://newsdata.io/api/1/news?apikey={newsAPIKey}&category=business,politics,technology&country=us&from_date={date}&to_date={date}"""
    
    return newsQuery



# Working

def getNews(date):

    dateString = f"{date.year}-{date.month}-{date.day}"
    resp = json.loads(requests.get(getNewsQuery(dateString)).text)

    

    res =  [[val['title'], val['pubDate']] for val in resp['results']]

    return res

# def getNewsTest():


#     resp = json.loads(requests.get(getNewsQuery()).text)

    

#     res =  [[val['title'], val['pubDate'], val["creator"], val["link"]] for val in resp['results']]

#     return res

