import json

class Message:
    def __init__(self, sender_username, text):
        self.sender_username = sender_username
        self.text = text

    def to_dict(self):
        return {'username': self.sender_username, 'text': self.text}

    def to_json(self):
        return json.dumps(self.to_dict())
