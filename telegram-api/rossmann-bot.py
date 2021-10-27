import os
import requests
import pandas as pd
import json

from flask import Flask, request, Response

# constants
TOKEN = '1951428412:AAFJVoz3tZlwm2ZH-3nVRb0NGBWK4NgFg2c'

# # Bot info
# https://api.telegram.org/bot1951428412:AAFJVoz3tZlwm2ZH-3nVRb0NGBWK4NgFg2c/getMe
#
# # Get updates
# https://api.telegram.org/bot1951428412:AAFJVoz3tZlwm2ZH-3nVRb0NGBWK4NgFg2c/getUpdates
#
# # Webwook
# https://api.telegram.org/bot1951428412:AAFJVoz3tZlwm2ZH-3nVRb0NGBWK4NgFg2c/setWebhook?url=https://c94402d480b726.localhost.run
#
# # Webwook Heroku
# https://api.telegram.org/bot1951428412:AAFJVoz3tZlwm2ZH-3nVRb0NGBWK4NgFg2c/setWebhook?url=https://rossmann-sales-bot.herokuapp.com
#
# # Send message
# https://api.telegram.org/bot1951428412:AAFJVoz3tZlwm2ZH-3nVRb0NGBWK4NgFg2c/sendMessage?chat_id=1781930753&text=Hi Debora, I am doing good, thks!

def send_message(chat_id, text):
    url = 'https://api.telegram.org/bot{}/'.format(TOKEN)
    url = url + 'sendMessage?chat_id={}'.format(chat_id)

    r = requests.post(url, json={'text': text})
    print('Status code {}'.format(r.status_code))

    return None


def load_dataset(store_id):
    # load test dataset
    df10 = pd.read_csv('test.csv')
    df_store_raw = pd.read_csv('store.csv')

    # merge dataset + store info
    df_test = pd.merge(df10, df_store_raw, how='left', on='Store')

    df_test = df_test[df_test['Store'] == store_id]

    if not df_test.empty:
        # remove closed days, null open day, drop id column
        df_test = df_test[df_test['Open'] != 0]
        df_test = df_test[~df_test['Open'].isnull()]
        df_test = df_test.drop('Id', axis=1)

        # convert DataFrame to JSON
        data = json.dumps(df_test.to_dict(orient='records'))

    else:
        data = 'error'

    return data


def predict(data):
    # API Call
    url = 'https://rossmann-sales-prediction-test.herokuapp.com/rossmann/predict'
    header = {'Content-type': 'application/json'}
    data = data

    r = requests.post(url, data=data, headers=header)
    print('Status Code {}'.format(r.status_code))

    # JSON to DataFrame
    d1 = pd.DataFrame(r.json(), columns=r.json()[0].keys())

    return d1


def parse_message(message):
    chat_id = message['message']['chat']['id']
    store_id = message['message']['text']

    store_id = store_id.replace('/', '')

    try:
        store_id = int(store_id)

    except ValueError:
        store_id = 'error'

    return chat_id, store_id


# API initialize
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.get_json()

        chat_id, store_id = parse_message(message)

        if store_id != 'error':
            # loading data
            data = load_dataset(store_id)

            if data != 'error':
                # prediction
                d1 = predict(data)

                # calculation
                d2 = d1[['store', 'prediction']].groupby('store').sum().reset_index() # accumulated sales by store

                # send message
                msg = 'Store number {} is going to sell {:,.2f} $ in the next 6 weeks'.format(d2['store'].values[0], d2['prediction'].values[0])
                send_message(chat_id, msg)
                return Response('Ok', status=200)

            else:
                send_message(chat_id, 'Store prediction unavailable')
                return Response('Ok', status=200)

        else:
            send_message(chat_id, 'Invalid store ID')
            return Response('Ok', status=200)

    else:
        return '<h1> Rossmann Telegram Bot </h1>'

if __name__=='__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)