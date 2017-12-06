from .. import Account


def get(user_name):
    return globals()[user_name.upper()]


USER1 = Account('user1', 'User One', password='UserOnePassword')


