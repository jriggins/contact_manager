import abc


class Repository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def all_accounts(self):
        pass

    @abc.abstractmethod
    def save(self, account):
        pass

    @abc.abstractmethod
    def find_by_account_id(self, account_id):
        pass

    @abc.abstractmethod
    def clear_all(self):
        pass


class InMemoryAccountRepository(Repository):
    def __init__(self):
        self._db = {}

    def all_accounts(self):
        return iter(self._db.values())

    def save(self, account):
        self._db[account.account_id] = account

    def find_by_account_id(self, account_id):
        return self._db.get(account_id, None)

    def clear_all(self):
        self._db = {}
