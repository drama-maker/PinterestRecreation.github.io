from flask import Flask, request
from flask_restful import Api, Resource
from marshmallow import ValidationError
from models.user import UserSchema

app = Flask(__name__)
api = Api(app)

user_schema = UserSchema()

class UserResource(Resource):
    def get(self, user_id=None):
        return {"message": f"GET request for user with id {user_id}"}

    def post(self):
        try:
            data = user_schema.load(request.json)
            return {"message": "User data validated successfully", "data": data}
        except ValidationError as err:
            return {"error": "Validation error", "message": err.messages}, 400

    def put(self, user_id):
        return {"message": f"PUT request for user with id {user_id}"}

    def delete(self, user_id):
        return {"message": f"DELETE request for user with id {user_id}"}

api.add_resource(UserResource, '/user', '/user/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
