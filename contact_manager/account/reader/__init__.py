class Reader(object):
    def __init__(self, repository):
        self._repo = repository

    def all_accounts(self):
        return self._repo.all_accounts()

    def find_user_by_user_name(self, user_name):
        return self._repo.find_user_by_user_name(user_name)

    def login(self):
        pass
