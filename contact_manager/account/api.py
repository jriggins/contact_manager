import bcrypt

from contact_manager.account import command, handler, model


class Api:
    @classmethod
    def _hash_password(cls, password):
        return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())

    @classmethod
    def _is_valid_password(cls, password, hashed_password):
        return bcrypt.checkpw(bytes(password, 'utf-8'), hashed_password)

    def __init__(self, repo):
        self._repo = repo
        self._handler = handler.CommandHandler(self._repo, self._hash_password)

    def register_account(self, command: command.RegisterAccount):
        self._handler.register_account(command)

    def login(self, command: command.Login):
        account = self._repo.find_by_email_address(command.email_address)
        if account and self._is_valid_password(command.password, account.hashed_password):
            return 'x'
        else:
            raise Exception


