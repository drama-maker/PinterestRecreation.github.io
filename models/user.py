from datetime import datetime

from marshmallow import Schema, fields, validates, ValidationError
import re

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    email = fields.Email(required=True)
    #TODO:
    # rest of fields based on iteration 1 simplified

    @validates("password")
    def validates_password(self, password: str):
        if len(password) < 8:
            raise ValidationError("Password should be at least 8 characters long.")

        special_character_regex = r"\W"
        special_characters_match = re.search(special_character_regex, password) #-> None | regex
        if special_characters_match is None:
            raise ValidationError("Password should contain at least one special character.")

        # TODO:
        # Capital letters
        # normal letters
        # numbers
