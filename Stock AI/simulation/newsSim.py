import datetime
import json
import newsapi
import sys

API_KEY = "9cd8b39b10164f56b769b99f9edda233"


connection = newsapi.NewsApiClient(api_key=API_KEY)



def getNewsTest():

    news = connection.get_everything(q='stocks',
                                        language='en',
                                        sort_by='relevancy',
                                        page=2)
    
    return [[new["title"], new["publishedAt"], new["url"]] for new in news["articles"]]


def getNews(date):



    dateString = convertDatetimeToString(date)

    

    if dateString:

        news = connection.get_everything(q='stocks',
                                            language='en',
                                            sort_by='relevancy',
                                            from_param=dateString,
                                            to=dateString,
                                            page=2)
        
        return [[new["title"], new["publishedAt"]] for new in news["articles"]]
    
    return []








def convertDatetimeToString(date: datetime.datetime):

    try:

        return date.strftime("%Y-%m-%d")
    
    except:
        return None
    

def convertStringToDateTime(string):

    try:
        return datetime.datetime.strptime(string, '%Y-%m-%d')
    
    except:
        print(sys.exc_info())
        pass
    

    try:
        dt = datetime.datetime.strptime(string, "%Y-%m-%dT%H:%M:%SZ")

        return dt
    
    except:
        print(sys.exc_info())
        return None