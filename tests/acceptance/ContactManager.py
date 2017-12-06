import contact_manager.account.handler as account_handler
import contact_manager.account.model.example as account_examples
import contact_manager.account.reader as account_reader
import contact_manager.account.repo as account_repo


class ContactManager:
    def __init__(self):
        repo = account_repo.InMemoryAccountRepository()
        self.account_read_model = account_reader.Reader(repo)
        self.account_command_handler = account_handler.CommandHandler(repo)

    def clear_all_users(self):
        self.account_command_handler.clear_all()
        assert list(self.account_read_model.all_accounts()) == [], 'There should be no Accounts in the system.'

    def register_user(self, user_key):
        account = account_examples.get(user_key)
        self.account_command_handler.register_account(account)

    def user_should_exist(self, user_name):
        account = self.account_read_model.find_user_by_user_name(user_name)
        assert account, 'Unable to find Account with username {0}'.format(user_name)

    def log_in(self, user_name):
        pass

    def logged_in_user(self):
        pass
