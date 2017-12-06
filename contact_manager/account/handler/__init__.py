class CommandHandler(object):
    def __init__(self, repository):
        self._repo = repository

    def clear_all(self):
        self._repo.clear_all()

    def register_account(self, account):
        self._repo.save(account)
