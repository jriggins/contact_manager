from contact_manager.account import api
from .. import Account


def get(key):
    return globals()[key.upper()]


USER1 = Account('111', 'user1@example.org', hashed_password=api.Api._hash_password('User1Password'))


