import requests
import math
from flask import Flask
import json


text = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text
currencies = json.loads(text)


for(currency) in currencies['Valute']:
    print(currency)



app = Flask(__name__)

@app.route("/")
def hello():
    text = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text
    currencies = json.loads(text)
    result = ''
    for currency in currencies['Valute']:
        result += str(currency)+'<br>'
    return result


if __name__ == '__main__':
    app.run