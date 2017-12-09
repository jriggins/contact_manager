class Account(object):
    def __init__(self, id: str, email_address: str, hashed_password: str=None):
        self.id = id
        self.email_address = email_address
        self.hashed_password = hashed_password

