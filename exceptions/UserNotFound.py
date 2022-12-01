class UserNotFound(Exception):
    def __init__(self, nickname):
        self.nickname = nickname
        self.message = f"User {nickname} not found"

    def __str__(self):
        return self.message
