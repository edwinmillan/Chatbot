import requests
import json


def get_ip_address():
    headers = {'Accept': 'application/json'}
    return json.loads(requests.get('https://ifconfig.co/', headers=headers).content)
