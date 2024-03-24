from marshmallow import Schema, fields
from datetime import datetime

class SearchHistory(Schema):
    searchQuery = fields.String(required=True)
    searchDate = fields.DateTime(required=True, default=datetime.now)