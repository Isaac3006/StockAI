import datetime
import pytz
import requests
from dateutil.relativedelta import relativedelta
import sys
import newsSim

import matplotlib.pyplot as plt





class Polygon:

    def __init__(self) -> None:
        
        self.newsTime = None
        self.STOP = 15
        self.API_KEY = "ag5FMzJ92wj8kgvuY4LHpiES_OG05A8z"



    def getTime(self):

        return self.newsTime



    def transact(self, stocksAffected, date):

        self.newsTime = self.convertStringToDatetime(date).replace(microsecond=0,second=0)

        prof = 0

        for stock, mode in stocksAffected:


            prof += self.brokerage(stock, mode)


        return prof






    def brokerage(self, stock, mode):

        nowDate = self.newsTime
        
        prices = self.getPrices(stock, nowDate)

        

        buyPrice, buySuccess = self.findClosestTimeForBuy(prices, nowDate)


        sellPrice, sellSuccess = self.findClosestTimeForSell(prices, nowDate)

        if buySuccess and sellSuccess:
            
        

            if mode == "r":
                return (sellPrice - buyPrice) / buyPrice
            
            else:
                return (buyPrice - sellPrice) / buyPrice
        
        return 0







    def regTimeStamp(self, timestamp_msec):
        timestamp_sec = int(timestamp_msec) / 1000  # Convert from milliseconds to seconds
        return datetime.datetime.fromtimestamp(timestamp_sec).replace(second=0, microsecond=0) # .time()


    def getPrices(self, stock, date):

        dateString = newsSim.convertDatetimeToString(date)

        # example query: 
        # https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-01-09?
        # adjusted=true&sort=asc&limit=120&apiKey=ag5FMzJ92wj8kgvuY4LHpiES_OG05A8z

        query = f"""https://api.polygon.io/v2/aggs/ticker/{stock}/range/5/minute/{dateString}/{dateString}?adjusted=true&sort=asc&apiKey={self.API_KEY}"""

        req = []

        try:
            req = requests.get(query).json()['results']

        except:
            pass

        res = {self.regTimeStamp(val['t']).time() : val['o'] for val in req}


        

        return res


    def findClosestTimeForBuy(self, hashMap, date):
        time = date



        for off in range(0, self.STOP):

            currDate: datetime.datetime = time + datetime.timedelta(minutes=off)

            currTim = currDate.time()

            if currTim in hashMap:
                return hashMap[currTim], True
        
        return None, False
            


    def findClosestTimeForSell(self, hashMap, date):

        time = date



        for off in range(self.STOP, self.STOP * 2):

            currDate: datetime.datetime = time + datetime.timedelta(minutes=off)

            currTim = currDate.time()

            if currTim in hashMap:
                return hashMap[currTim], True
            

        
        return None, False
            

        



 

    def convertStringToDatetime(self, dateString):
        return newsSim.convertStringToDateTime(dateString)

    def convertDatetimeToString(self, date):
        return newsSim.convertDatetimeToString(date)



    def plot(self, stock, date):


        import matplotlib.pyplot as plt

        import datetime
        # Assuming data is your dictionary
        data = self.getPrices(stock, date)

        # convert the time to minutes past midnight for easier plotting
        x = [time.hour * 60 + time.minute for time in data.keys()]
        y = list(data.values())

        plt.figure(figsize=(15, 7))
        plt.plot(x, y, marker='o')

        # format the x-ticks to be in hours:minutes format
        plt.xticks(range(0, max(x), 60), [f'{i}:00' for i in range(24)])
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title('Time Series Data')
        plt.grid(True)

        plt.show()

    # print(getPrices())



        



    # print(sorted([self.regTimeStamp(val['t']) for val in res]))



    # print(res)


