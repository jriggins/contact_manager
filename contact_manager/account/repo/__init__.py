class InMemoryAccountRepository(object):
    def __init__(self):
        self._db = {}

    def all_accounts(self):
        return iter(self._db.values())

    def save(self, account):
        self._db[account.user_name] = account

    def find_user_by_user_name(self, user_name):
        return self._db.get(user_name, None)

    def clear_all(self):
        self._db = {}
