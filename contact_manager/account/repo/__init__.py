import abc


class Repository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def all_accounts(self):
        pass

    @abc.abstractmethod
    def save(self, account):
        pass

    @abc.abstractmethod
    def find_user_by_email_address(self, email_address):
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
        self._db[account.email_address] = account

    def find_user_by_email_address(self, email_address):
        return self._db.get(email_address, None)

    def clear_all(self):
        self._db = {}
