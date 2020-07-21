import requests


def send_to_telegram(app_token, userid, message):
    url="https://api.telegram.org/bot{token}".format(token=app_token)
    payload = {
        'chat_id': userid,
        'text': message,
        'parse_mode': 'Markdown'
    }

    try:
         requests.post("{url}/sendMessage".format(url=url),json=payload)
    except ConnectionError as e:
         print("ConnectionError")
         return False
    return True
