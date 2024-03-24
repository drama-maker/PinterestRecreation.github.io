from models.profilevisibility import ProfileVisibility

class ProfileVisibility(Schema):
    isPrivateProfile = fields.Boolean(required=False, default=False)
    isSearchPrivacy = fields.Boolean(required=False, default=False)