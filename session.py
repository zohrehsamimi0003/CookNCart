class Session:
    def __init__(self, db):
        self.db = db
        self.user = None

    def set_user(self, user):
        """Sets the user attribute"""
        self.user = user