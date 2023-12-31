import json
import newsapi

API_KEY = ""


connection = newsapi.NewsApiClient(api_key=API_KEY)



def getNewsTest():

    news = connection.get_everything(q='stocks',
                                        language='en',
                                        sort_by='relevancy',
                                        page=2)
    
    return [[new["title"], new["publishedAt"], new["url"]] for new in news["articles"]]


def getNews():

    news = connection.get_everything(q='stocks',
                                        language='en',
                                        sort_by='relevancy',
                                        page=2)
    
    return [[new["title"], new["publishedAt"]] for new in news["articles"]]




for val in getNews():

    print(val) 

    print()

    print()



