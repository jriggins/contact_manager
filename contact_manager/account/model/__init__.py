class Account(object):
    def __init__(self, user_name, name, password=None):
        self.user_name = user_name
        self.name = name
        self.hashed_password = self.hash_password(password)

    def hash_password(self, password):
        return password
