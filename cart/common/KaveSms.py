from operator import truediv

from kavenegar import *
from urllib.error import HTTPError


# Send SMS with token
def send_sms_with_template(receptor, tokens:dict, template):
    try:
        api = KavenegarAPI('6E465A78557030392F4C74754479576C4469786557324D6D6C58632B49477232684230767A434D565961553D')
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
        api = KavenegarAPI('6E465A78557030392F4C74754479576C4469786557324D6D6C58632B49477232684230767A434D565961553D')
        params_buyer = {
            'receptor': receptor,
            'message': message,
            'sender': '2000660110'
        }
        response = api.sms_send(params_buyer)
        print(response)

    except APIException as e:
        print(e)

    except HTTPError as e:
        print(e)
