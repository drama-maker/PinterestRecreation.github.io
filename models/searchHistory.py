from models.searchHistory import SearchHistory

class SearchHistory(Schema):
    searchQuery = fields.String(required=True)
    searchDate = fields.DateTime(required=True, default=datetime.now())