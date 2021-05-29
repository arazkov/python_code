import requests as rq


def answer(question):
    if question.lower() == 'ip':
        send_result = rq.get(
            'https://api.telegram.org/'
            'bot1471638513:AAESV-K1iuiG_n3ZO6F7LRpM-vQKYrfxc78/'
            'sendMessage',
             params={
                'chat_id': chat_id, 
                'text': f'IP {ip}'
                    }
            ) 
    elif question.lower() == 'weather' or question.lower() == 'погода':
        send_result = rq.get(
            'https://api.telegram.org/'
            'bot1471638513:AAESV-K1iuiG_n3ZO6F7LRpM-vQKYrfxc78/'
            'sendMessage',
             params={
                'chat_id': chat_id, 
                'text': f'Погода в {what_weather(what_city(ip))}'
                    }
            )
    else:
        send_result = rq.get(
            'https://api.telegram.org/'
            'bot1471638513:AAESV-K1iuiG_n3ZO6F7LRpM-vQKYrfxc78/'
            'sendMessage',
             params={
                'chat_id': chat_id, 
                'text': f'Привет {autor_name.capitalize()}'
                    }
            )
    return send_result
    

def what_city(ip):
    result = rq.get(f'http://ip-api.com/json/{ip}?lang=ru').json()
    #result2 = result.json()
    return result['city']

def what_weather(city):
    url = f'http://wttr.in/{city}'
    weather_parameters = {
        'format': 3,
        'M': ''
    }
    try:
        response = rq.get(url, params=weather_parameters)
    except rq.ConnectionError:
        return '<сетевая ошибка>'
    if response.status_code == 200:
        return response.text.strip()
    else:
        return '<ошибка на сервере погоды. попробуйте позже>'




ip = rq.get('https://api.ipify.org').text

last_update_id = 0
while True:
    url = rq.get(
        'https://api.telegram.org/'
        'bot1471638513:AAESV-K1iuiG_n3ZO6F7LRpM-vQKYrfxc78/'
        'getUpdates', 
         params={'offset': last_update_id + 1})
    
    data = url.json()
    for update in data['result']:
        print(update['message']['text'])
        message = update['message']['text']
        last_update_id = update['update_id']
        chat_id = update['message']['chat']['id']
        autor_name = update['message']['chat']['first_name']
        answer(message)
