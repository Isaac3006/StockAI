import sys
sys.path.insert(0, r"C:\Users\isaac\OneDrive\Desktop\Todos\Codes\Real world projects\Stock AI")
import requests
import os
import openai
import time
import datetime
import json 
from googletrans import Translator
import AI
import google.generativeai as palm
import asyncio
import yfinance as yf
from polygon import Polygon
import newsSim

# TODO Investigar cuales news sources tiene el news API en estados unidos 
# (si no tiene los importantes maybe) reconsidera usar otro
# TODO considera nadamas usar esto para noticias que cambiaran el mundo como el inicio de la guerra mundial el problema es como saber si eres el primero
# TODO las noticias no tienen las horas universales asi que tienes que somehow entender como saber si la noticia
# en verdad es nueva o no quiza solo usando noticias americanas o algo asi
# TODO considera hacer que el analisis de las noticias sean multithreaded
# TODO analizar este sistema para crypto ya que es mas volatil que stocks
# TODO considera expandirte a mercados con menos algorithmic traders para que haya menos competencia
# TODO quiza modifica "seen" para que en vez de ver si ya viste la noticia mire si ya usaste ese stock recently
# porque los odds que hayan 2 noticias within 15 min que sean diferentes son minimos
# TODO how to run this code in the cloud

# TODO pon algo que resells the stock after x number of minutes (around 15 ish?)
# TODO considera hacer una simulacion para evaluar si esto te haria plata y hazlo a base de GPT xq gpt no sabe 
# que paso despues del 21
# Usa quandl para las simulaciones!!!
# TODO considera usar mas AIs que analizen la noticia como por ejemplo los otros GPTs o davinchi o otros


# TODO recuerda agregar short option a brokerage
# TODO recuerda agregar lo de no repetir stocks within 30 minutes or something
# TODO TODO puedes hacer que chatgpt analize si una noticia va a cambiar extremadamente el precio de una accion o no y lo haces como un numero del 1 a 10
# TODO la calidad de las noticias es extremadamente baja y x eso es que las cosas no van bien quiza este api
# ayude: https://rapidapi.com/blog/breaking-news-api-with-python-php-ruby-javascript-examples/#:~:text=The%20Breaking%20News%20Application%20Programming%20Interface%20allows%20programmers,company%20news%20feed%20retrieval%20across%20different%20news%20sources.

# newsTemplate = [['BCPG พร้อมพันธมิตร PSDC จัดพิธีวางศิลาฤกษ์ อาคาร Samyan District Cooling by PMCU', '2023-06-15 04:10:2       29'], ['Pour avoir caricaturé Dakaractu: Siaka Ndong et le journal "la Dépêche Républicaine" condamnés à 2 mois de prison assortis du sursis et 2 millions de FCFA de dommages et intérêts', '2023-06-15 04:08:32'], ['Nákupy v Poľsku: Slováci okrem lacných potravín chodia teraz vo veľkom nakupovať aj iný tovar', '2023-06-15 04:07:59'], ['זה כנראה הדבר הכי מדהים שמצאו בחפירות ארכיאולוגיות בישראל. לחיים!', '2023-06-15 04:07:58'], ['מכבי פ"ת עוקבת אחרי מגן מכבי חיפה', '2023-06-15 04:07:58'], ['כל הפרטים לגבי מצבו של אברמוב בבית"ר ירושלים וחיזוק הקבוצה הקיץ', '2023-06-15 04:07:58'], ["אמבפה רוצה לסיים חוזה בפ.ס.ז', שמתעקשת למכור אותו. הכוכב שוקל צעד מפתיע", '2023-06-15 04:07:58'], ['US plays down chance of breakthrough from Blinken China visit after tense call', '2023-06-15 04:06:56'], ['How Much Should YOU Invest In Low Caps? (Big Week For Crypto)', '2023-06-15 04:06:27'], ['Destacan en Venezuela impronta de Bolívar en Martí y Fidel en Chávez', '2023-06-15 04:05:23']]

# howOldCanNewsBe = 15

# delayBetweenChecks= 1

# MICROSECOND_TO_SECOND = 1000000

recordFile = r"C:\Users\isaac\OneDrive\Desktop\Todos\Codes\Real world projects\Stock AI\simulation\records.csv"

howOldCanNewsBe = 15

brokerage = Polygon()


translator = Translator()

today = datetime.datetime(2023, 6, 30) # 2023-05-17


seen = set()

prof = 0

# messages=[
#         {"role": "user", "content": "hi"}

#     ]



async def main():
    global today
    global brokerage
    global seen
    global prof
 
    # while True:

    file = open(recordFile, "a")
    for _ in range(5):

        


        # start = datetime.datetime.now()

        news = newsSim.getNews(today)

        for title, date in news:
            if not isNew(date) or title in seen:
                continue

            seen.add(title)



            title = f""" \" {title} \" """

            gpt, bard = await AI.analyze(title)

            stocksAffected = {}

            profit = 0

            if gpt and bard:

                stocksAffected = actions(gpt, bard)

                profit = brokerage.transact(stocksAffected, date)

                prof += profit


            recordTransactions(title, gpt, bard, stocksAffected, profit, file)

        # end = datetime.datetime.now()


        # wait = delayBetweenChecks - (end - start).microseconds / MICROSECOND_TO_SECOND

    file.close()

        
    
    today += datetime.timedelta(days=1)
        # time.sleep(max(wait * 60, 0))

def actions(gptResponse, bardResponse):

    res = []


    for stock, change in gptResponse.items():

        if stock in bardResponse and bardResponse[stock] == change:

           res.append([stock, change])

    

    return res



def isNew(news):

    try:


        released = newsSim.convertStringToDateTime(news)




        return (today - released).total_seconds() // 60 < howOldCanNewsBe
    
    except:

        return False












def recordTransactions(title, gptResponse, bardResponse, stocksAffected, profit, file):

    title = title[3:-3]

    

    try:
        trans = translator.translate(title)
        file.write(f"{profit},{trans.text},{stocksAffected},{gptResponse},{bardResponse}\n")
    except:
        pass


    try:
        file.write(f"{profit},{title},{stocksAffected},{gptResponse},{bardResponse}\n")
    except:
        pass


        






    



asyncio.run(main())