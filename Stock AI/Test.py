import requests
import os
import openai
import json
import main
import AI
import google.generativeai as palm
import unittest


howOldCanNewsBe = 15


openaiKey = "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"

newsAPIKey = "pub_2439147b28baa2832e2c4e762e702dd89dd0f"

testQuery = "https://newsdata.io/api/1/news?apikey=pub_2439147b28baa2832e2c4e762e702dd89dd0f&"


newsQuery = f"https://newsdata.io/api/1/news?apikey={newsAPIKey}&category=business,politics,technology"
defaultMessage = """




You are going to decide a news will either make some stock rise, fall or depends. 
There is also a posibility that the title of the news will have nothing to do with stocks. 
Format your answer in the following way: `{"stockName": "change", \"stockName\": \"change\" ... }`. 
If the stock will rise replace "change" with \"r\" and if it will fall replace it with \"f\". 
The stock name should be the abbreviation of the stock market. The news you are going to react to is 


"""

news = """ \"  \" """
openai.api_key = os.getenv(openaiKey)





def newsapi():

    print(main.getNews(testQuery))



def test():


    newsapi()
    # gpt()

def gpt():

    print(main.GPT(""))


def p():

    print()





def modelsBard():

    print(palm.list_models)






modelsBard()