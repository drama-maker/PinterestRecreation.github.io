from datetime import datetime
from marshmallow import Schema, fields, validates, ValidationError
import re

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    email = fields.Email(required=True)
    registrationDate = fields.DateTime(required=True, default=datetime.now)
    profilePic = fields.Url(required=False)
    firstName = fields.String(required=True)
    lastName = fields.String(required=False)
    birthdate = fields.DateTime(required=True)
    gender = fields.String(required=False)
    pronouns = fields.String(required=True)
    country = fields.String(required=True)
    language = fields.String(required=True)
    about = fields.String(required=False)
    websiteURL = fields.Url(required=False)
    isDeactivated = fields.Boolean(required=True, default=False)
    isDeleted = fields.Boolean(required=True, default=False)

    @validates("password")
    def validate_password(self, password: str):
        if len(password) < 8:
            raise ValidationError("Password should be at least 8 characters long.")

        special_character_regex = r"\W"
        if not re.search(special_character_regex, password):
            raise ValidationError("Password should contain at least one special character.")

        if not any(char.isupper() for char in password):
            raise ValidationError("Password should contain at least one uppercase letter.")

        if not any(char.islower() for char in password):
            raise ValidationError("Password should contain at least one lowercase letter.")

        if not any(char.isdigit() for char in password):
            raise ValidationError("Password should contain at least one digit.")

    @validates("email")
    def validate_email(self, email: str):
        email_regex = r'^\S+@\S+\.\S+$'
        if not re.match(email_regex, email):
            raise ValidationError("Invalid email address.")
        
    @validates("birthdate")
    def validate_birthdate(self, birthdate: datetime):
        if birthdate >= datetime.now():
            raise ValidationError("Birthdate must be in the past.")
        if (datetime.now() - self.context.get('birthdate')).days < 16 * 365:
            raise ValidationError("You have to be 16 or older.")

class ProfileVisibility(Schema):
    isPrivateProfile = fields.Boolean(required=True, default=False)
    isSearchPrivacy = fields.Boolean(required=True, default=False)
    
class Pins(Schema):
    title = fields.String(required=True)
    description = fields.String(required=False)
    imageURL = fields.Url(required=True)
    searchKeywords = fields.List(fields.String(), required=False)
    createdAt = fields.DateTime(required=True, default=datetime.now)
    isDeleted = fields.Boolean(required=True, default=False)
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

class SearchHistory(Schema):
    searchQuery = fields.String(required=True)
    searchDate = fields.DateTime(required=True, default=datetime.now())
