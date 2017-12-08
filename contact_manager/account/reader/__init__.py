from contact_manager.account import repo


class Reader(object):
    def __init__(self, repository: repo.Repository):
        self._repo = repository

    def all_accounts(self):
        return self._repo.all_accounts()

    def find_user_by_email_address(self, email_address):
        return self._repo.find_user_by_email_address(email_address)
