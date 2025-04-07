from decouple import config

from kavenegar import *
from urllib.error import HTTPError


# Send SMS with token
def send_sms_with_template(receptor, tokens:dict, template):
    try:
        api = KavenegarAPI(config('KAVENEGAR_API_KEY'))
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
        api = KavenegarAPI(config('KAVENEGAR_API_KEY'))
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
