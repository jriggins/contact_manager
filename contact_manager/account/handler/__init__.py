from contact_manager.account import command, model, repo


class CommandHandler(object):
    def __init__(self, repository: repo.Repository):
        self._repo = repository

    def clear_all(self):
        self._repo.clear_all()

    def register_account(self, command: command.RegisterAccount):
        account = model.Account(command.email_address, command.password)
        self._repo.save(account)

    def handle_Login(self, command: command.Login):
        account = self._repo.find_user_by_email_address(command.email_address)
        if account.is_valid_password(command.password):
            self._repo.create_session(account)
