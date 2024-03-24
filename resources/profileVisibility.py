from marshmallow import Schema, fields

class ProfileVisibility(Schema):
    isPrivateProfile = fields.Boolean(required=False, default=False)
    isSearchPrivacy = fields.Boolean(required=False, default=False)
