from flask_restful import Resource, reqparse
from chatbot.api import api


class Root(Resource):
    def get(self):
        return {'Status': '200 OK'}, 200


api.add_resource(Root, '/')