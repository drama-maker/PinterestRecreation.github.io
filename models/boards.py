from models.boards import Board

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
