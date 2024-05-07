class Session:
    def __init__(self, main_win, my_db):
        self.my_db = my_db
        self.main_win = main_win
        self.user = None

    def set_user(self, user):
        self.user = user