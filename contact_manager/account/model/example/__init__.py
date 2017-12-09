from .. import Account


def get(user_name):
    return globals()[user_name.upper()]


USER1 = Account('111', 'user1', password='UserOnePassword')


