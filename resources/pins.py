import re
from datetime import datetime
from marshmallow import Schema, fields, validates, ValidationError
from models.pins import Pins

class PinsSchema(Schema):
    title = fields.String(required=True)
    description = fields.String(required=False)
    imageURL = fields.Url(required=True)
    searchKeywords = fields.List(fields.String(), required=False)
    createdAt = fields.DateTime(required=False, default=datetime.now)
    isDeleted = fields.Boolean(required=False, default=False)
    swear_words = ["swear1", "swear2", "swear3"]  # TODO: Add list of swear words
    
    @validates("title")
    def validate_title(self, title: str):
        self._check_swear_words(title)

    @validates("description")
    def validate_description(self, description: str):
        self._check_swear_words(description)

    @validates("searchKeywords")
    def validate_keywords(self, keywords: list):
        for keyword in keywords:
            self._check_swear_words(keyword)

    def _check_swear_words(self, text: str):
        for swear_word in self.swear_words:
            if re.search(rf'\b{re.escape(swear_word)}\b', text, re.IGNORECASE):
                raise ValidationError(f"Swear words are not allowed.")

class PinsResource(Resource):
    def get(self, pin_id=None):
        return {"message": f"GET request for pin with id {pin_id}"}

    def post(self):
        try:
            data = PinsSchema().load(request.json)
            created_pin = Pins.create(**data)
            return {"message": "Pin created successfully", "data": created_pin}
        except ValidationError as err:
            return {"error": "Validation error", "message": err.messages}, 400

    def put(self, pin_id):
        try:
            data = PinsSchema().load(request.json)
            updated_pin = Pins.update(pin_id, **data)
            return {"message": "Pin updated successfully", "data": updated_pin}
        except ValidationError as err:
            return {"error": "Validation error", "message": err.messages}, 400

    def delete(self, pin_id):
        Pins.delete(pin_id)
        return {"message": "Pin deleted successfully"}

api.add_resource(PinsResource, '/pin', '/pin/<int:pin_id>')