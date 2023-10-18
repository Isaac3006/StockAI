import sys
import requests
import os
import openai
import time
import datetime
import json
from googletrans import Translator
import AI
import brokerage
import newsAPI
import google.generativeai as palm
import asyncio
import yfinance as yf



# TODO Investigar cuales news sources tiene el news API en estados unidos 
# (si no tiene los importantes maybe) reconsidera usar otro
# TODO newsAPI.org acepta segundos!!
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
# TODO!!! ChatGPT provided the entire London Stock Exchange as something that will drop so either you need to take
# it into account and make it be maybe the top 10 stocks in england or tell it to not do that and instead send the top
# 5 stocks in england

# TODO recuerda agregar short option a brokerage

newsTemplate = [['BCPG พร้อมพันธมิตร PSDC จัดพิธีวางศิลาฤกษ์ อาคาร Samyan District Cooling by PMCU', '2023-06-15 04:10:2       29'], ['Pour avoir caricaturé Dakaractu: Siaka Ndong et le journal "la Dépêche Républicaine" condamnés à 2 mois de prison assortis du sursis et 2 millions de FCFA de dommages et intérêts', '2023-06-15 04:08:32'], ['Nákupy v Poľsku: Slováci okrem lacných potravín chodia teraz vo veľkom nakupovať aj iný tovar', '2023-06-15 04:07:59'], ['זה כנראה הדבר הכי מדהים שמצאו בחפירות ארכיאולוגיות בישראל. לחיים!', '2023-06-15 04:07:58'], ['מכבי פ"ת עוקבת אחרי מגן מכבי חיפה', '2023-06-15 04:07:58'], ['כל הפרטים לגבי מצבו של אברמוב בבית"ר ירושלים וחיזוק הקבוצה הקיץ', '2023-06-15 04:07:58'], ["אמבפה רוצה לסיים חוזה בפ.ס.ז', שמתעקשת למכור אותו. הכוכב שוקל צעד מפתיע", '2023-06-15 04:07:58'], ['US plays down chance of breakthrough from Blinken China visit after tense call', '2023-06-15 04:06:56'], ['How Much Should YOU Invest In Low Caps? (Big Week For Crypto)', '2023-06-15 04:06:27'], ['Destacan en Venezuela impronta de Bolívar en Martí y Fidel en Chávez', '2023-06-15 04:05:23']]

howOldCanNewsBe = 15

delayBetweenChecks= 1

MICROSECOND_TO_SECOND = 1000000

recordFile = "records.csv"





translator = Translator()


# openai.api_key = os.getenv(openaiKey)


seen = set()


messages=[
        {"role": "user", "content": "hi"}

    ]



async def main():
    
 
    # while True:
    for _ in range(5):

        file = open(recordFile, "a")


        start = datetime.datetime.now()

        news = newsAPI.getNews()

        for title, date in news:
            if not isNew(date) and title not in seen:
                continue

            seen.add(title)



            title = f""" \" {title} \" """

            gpt, bard = await AI.analyze(title)

            stocksAffected = {}

            if gpt and bard:

                stocksAffected = actions(gpt, bard)

                brokerage.transact(stocksAffected)


            recordTransactions(title, gpt, bard, stocksAffected, file)

        end = datetime.datetime.now()


        wait = delayBetweenChecks - (end - start).microseconds / MICROSECOND_TO_SECOND

        file.close()
        # time.sleep(max(wait * 60, 0))

def actions(gptResponse, bardResponse):

    res = []


    for stock, change in gptResponse.items():

        if stock in bardResponse and bardResponse[stock] == change:

           res.append([stock, change])

    

    return res



def isNew(news):


    try:

        currentDate = datetime.datetime.now()

        released = convertToDatetime(news)




        return (currentDate - released).total_seconds() // 60 < howOldCanNewsBe
    
    except:

        return False




def convertToDatetime(string):

    try:
        return datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
    
    except:
        return datetime.datetime.now() - datetime.timedelta(days=2)










def recordTransactions(title, gptResponse, bardResponse, stocksAffected, file):

    title = title[3:-3]

    for stock, mode in stocksAffected:

        try:
            trans = translator.translate(title)
            file.write(f"{trans.text},{stock},{mode},{gptResponse},{bardResponse}\n")
        except:
            print(title)







    



# asyncio.run(main())