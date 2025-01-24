from operator import truediv

from kavenegar import *
from urllib.error import HTTPError


# Send SMS with token
def send_sms_with_template(receptor, tokens:dict, template):
    try:
        api = KavenegarAPI('5353674B775641774A757843304F666479464D786648645553495845504C6A342B4A6D426C6967585777553D')
        params = {
            'receptor': receptor,
            'template': template,
        }
        for key,value in tokens.items():
            params[key] = value
        response = api.verify_lookup(params)
        print(response)
        return True

    except APIException as e:
        print(e)
        return False

    except HTTPError as e:
        print(e)
        return False

# Send normal SMS(without Token)
def send_sms_normal(receptor, message):
    try:
        api = KavenegarAPI('5353674B775641774A757843304F666479464D786648645553495845504C6A342B4A6D426C6967585777553D')
        params_buyer = {
            'receptor': receptor,
            'message': message,
            'sender': '',
        }
        response = api.sms_send(params_buyer)
        print(response)

    except APIException as e:
        print(e)

    except HTTPError as e:
        print(e)
