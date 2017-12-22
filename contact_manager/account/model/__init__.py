class Account(object):
    def __init__(self, id: str, account_id: str, hashed_password: str=None):
        self.id = id
        self.account_id = account_id
        self.hashed_password = hashed_password

