class Account(object):
    def __init__(self, email_address, password=None):
        self.email_address = email_address
        self.hashed_password = self.hash_password(password)

    def hash_password(self, password):
        return password
