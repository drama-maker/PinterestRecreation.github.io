from flask import Flask, request
from flask_restful import Api, Resource
from marshmallow import ValidationError
from models.user import UserSchema

app = Flask(__name__)
api = Api(app)

user_schema = UserSchema()

if __name__ == '__main__':
    app.run(debug=True)
