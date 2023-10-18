import requests

real = False

ACCOUNT_ID = ""

TOKEN = ""


ACCOUNT_ID_PAPER = ""

TOKEN_PAPER = ""


URL = f'https://api.tradier.com/v1/accounts/{ACCOUNT_ID}/orders'

URL_PAPER = f"https://sandbox.tradier.com/v1/accounts/{ACCOUNT_ID_PAPER}/orders"


def transact(stocksAffected):
    

    for stock, mode in stocksAffected:


        brokerage(stock, mode)



def brokerage(stock, mode):
    

    response = requests.post(getURL(),
    data={'class': 'equity', 'symbol': stock, 'side': 'buy', 'quantity': getQuantityByPrice(stock), 'type': 'market', 'duration': 'day'},
    headers={'Authorization': f'Bearer {getToken()}', 'Accept': 'application/json'}


)
    
    print(response.text)


def getQuantityByPrice(stock):
    return "1"

def getUserInfo():

    
    response = requests.get('https://api.tradier.com/v1/user/profile',
        params={},
        headers={'Authorization': f'Bearer {getToken()}', 'Accept': 'application/json'}
    )
    json_response = response.json()
    print(response.status_code)
    print(json_response)


def getToken():

    return TOKEN if real else TOKEN_PAPER


def getAccountId():
    return ACCOUNT_ID if real else ACCOUNT_ID_PAPER


def getURL():
    return URL if real else URL_PAPER