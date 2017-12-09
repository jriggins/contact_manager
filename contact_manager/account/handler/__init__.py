from contact_manager.account import command, model, repo


class CommandHandler(object):
    def __init__(self, repository: repo.Repository, hash_password):
        self._repo = repository
        self._hash_password = hash_password

    def clear_all(self):
        self._repo.clear_all()

    def register_account(self, command: command.RegisterAccount):
        account = model.Account(command.id, command.email_address, self._hash_password(command.password))
        self._repo.save(account)

