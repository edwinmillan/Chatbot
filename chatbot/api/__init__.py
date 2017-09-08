from flask_restful import Api
from chatbot import app

api = Api(app)

import chatbot.api.resources