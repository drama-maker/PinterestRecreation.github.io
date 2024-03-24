from models.pins import Pins

class Pins(Schema):
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
    