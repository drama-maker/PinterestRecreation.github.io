from flask import request
from flask_restful import Resource
from models.user import UserSchema

users = [
    {
        "id": 1,
        "username": "user1",
        "password": "password123!",
        "email": "test@mail.com"
    },
{
        "id": 2,
        "username": "user2",
        "password": "password123!",
        "email": "test@mail.com"
    },
{
        "id": 3,
        "username": "user3",
        "password": "password123!",
        "email": "test@mail.com"
    }
]

class User(Resource):
    def get(self, user_id=None):
        users_list = users
        if user_id:
            for user in users:
                if user_id == user["id"]:
                    return UserSchema().dump(user)

        return {
            "data": UserSchema(many=True).dump(users_list)
        }

    def post(self):
        index_u = None
        data = request.get_json()
        user = UserSchema().load(data)
        user['id'] = users[-1]['id'] +1
        user = UserSchema().dump(user)
        users.append(user)
        return user

    def put(self, user_id: int):
        data = request.get_json()
        user = None
        for u in users:
            if user_id == u["id"]:
                index_u = users.index(u)
                user = UserSchema().dump(u)
        for key in data.keys():
             user[key] = data[key]

        users[index_u] = user


        return user

    def delete(self, user_id: int):
        for u in users:
            if user_id == u["id"]:
                index_u = users.index(u)
        users.pop(index_u)

        return 204
