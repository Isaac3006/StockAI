# INCONISTENT

from newscatcherapi import NewsCatcherApiClient


API_KEY = 'tJgp0mCZ8TYADd5TX0_j5riJigxb-m3dp3CiLycOYUk'

newscatcherapi = NewsCatcherApiClient(x_api_key=API_KEY)


def getNews():

    all_articles = newscatcherapi.get_search(q='Elon Musk',
                                            lang='en',
                                            countries='CA',
                                            page_size=100)
    

    res = []
    

    for article in all_articles['articles']:

        if article['published_date_precision'] == 'full':
            res.append([article['title'], article['published_date']])

    res.sort(key=lambda x: x[1])
    return res

x =  getNews()
[print(new) for new in x]
print(len(x))



