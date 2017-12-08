from contact_manager.account import command, handler, model


class Api:
    def __init__(self, repo):
        self._repo = repo
        self._handler = handler.CommandHandler(self._repo)

    def register_account(self, command: command.RegisterAccount):
        self._handler.register_account(command)

    def login(self, command: command.Login):
        account = self._repo.find_by_email_address(command.email_address)
