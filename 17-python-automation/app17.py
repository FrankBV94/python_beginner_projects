#TODO: Revisar error de coneccion(proxy) 
import requests
import schedule
import time

proxies = {
    'http': 'http://10.9.12.26:3128',
}


def send_message():
    resp = requests.post('http://textbelt.com/text', {
        'phone': 53390100,
        'message': 'Aloha',
        'key': 'textbelt'
    })

    print(resp.json())

# schedule.every().day.at('10:00').do(send_message)


schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
