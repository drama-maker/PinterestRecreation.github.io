from flask import request, abort, Response
from flask_restful import Resource
from models.user import UserSchema
from app.database import db
from resources.user import UserResource

class User(Resource):
    def _find_user(self, user_id):
        user = db.user.find_unique(
            where={
                'id': user_id
            }
        )
        
        if user is None:
            abort(404, "User not found")
            
        return user
                
    def get(self, user_id=None):
        if user_id:
            user = self._find_user(user_id)
                
            return UserSchema().dump(user)

        users_list = db.user.find_many()
        return {
            "data": UserSchema(many=True).dump(users_list)
        }

    def post(self):
        data = request.get_json()
        user = UserSchema().load(data)
        created_user = db.user.create(
            data= user
        )
        return UserSchema().dump(created_user)

    def put(self, user_id: int):
        data = request.get_json()
        user = self._find_user(user_id)
        updated_user = db.user.update(
            where={
                'id': user.id
            },
            data=data
        )
        
        return UserSchema().dump(updated_user)

    def delete(self, user_id: int):
        user = self._find_user(user_id)
        db.user.delete(
            where={
                'id': user.id
            }
        )
        return 204

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