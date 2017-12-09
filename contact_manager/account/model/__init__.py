class Account(object):
    def __init__(self, email_address, hashed_password=None):
        self.email_address = email_address
        self.hashed_password = hashed_password

