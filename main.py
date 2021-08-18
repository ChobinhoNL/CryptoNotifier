from plyer import notification
import time
from requests import Request, Session
import json

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
parameters = {
    # Which crypto do we want?
    "symbol": "ADA",
    "convert": "EUR",
}

headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": "c6281de5-c308-44ac-8e1b-cc5e66691086"
}

session = Session()
session.headers.update(headers)

def get_price():
    response = session.get(url, params=parameters)
    price = (json.loads(response.text)["data"]['ADA']['quote']['EUR']['price'])
    price = "{:.2f}".format(price)
    price = f"€ {price}"
    return price


def notifyMe(title, message):
    notification.notify(
        title = title,
        message = f"The actual price for ADA is {message}",
        app_icon = "cryptologo.ico",
        timeout = 5,
    )

if __name__ == '__main__':
    while True:
        act = get_price()
        notifyMe("ADA", act)
        sleep = 0
        min = 0
        while sleep != 900:
            time.sleep(60)
            sleep += 60
            min += 1
            print(f"{min} minutes have passed.")