import json
from flask import request
from flask_restful import Resource
from chatbot.api import api
from chatbot.api.get_ip_address import get_ip_address


class Root(Resource):
    def get(self):
        return {'Status': '200 OK'}, 200

    def post(self):
        payload = request.form
        return {'echo': payload}, 200


class IPAddress(Resource):
    def get(self):
        return get_ip_address(), 200


class HipChat(Resource):
    def post(self):
        payload = json.loads(request.data)
        message = payload['item']['message']['message'].replace('/chatbot ', '')

        formatted_message = {
            'color': 'green',
            'message': message,
            'notify': False,
            'message_format': 'text'
        }
        return formatted_message


api.add_resource(Root, '/')
api.add_resource(IPAddress, '/ip')
api.add_resource(HipChat, '/hipchat')
