import re
from marshmallow import Schema, fields, validates, ValidationError
from models.boards import Boards as Board

class Boards(Schema):
    name = fields.String(required=True)
    swear_words = ["swear1", "swear2", "swear3"]  # TODO: Add list of swear words
    
    @validates("name")
    def validate_name(self, name: str):
        self._check_swear_words(name)

    def _check_swear_words(self, text: str):
        for swear_word in self.swear_words:
            if re.search(rf'\b{re.escape(swear_word)}\b', text, re.IGNORECASE):
                raise ValidationError(f"Swear words are not allowed.")

class BoardsResource(Resource):
    def get(self, board_id=None):
        return {"message": f"GET request for board with id {board_id}"}

    def post(self):
        try:
            data = Boards().load(request.json)
            created_board = Board.create(**data)
            return {"message": "Board created successfully", "data": created_board}
        except ValidationError as err:
            return {"error": "Validation error", "message": err.messages}, 400

    def put(self, board_id):
        try:
            data = Boards().load(request.json)
            updated_board = Board.update(board_id, **data)
            return {"message": "Board updated successfully", "data": updated_board}
        except ValidationError as err:
            return {"error": "Validation error", "message": err.messages}, 400

    def delete(self, board_id):
        Board.delete(board_id)
        return {"message": "Board deleted successfully"}

api.add_resource(BoardsResource, '/board', '/board/<int:board_id>')