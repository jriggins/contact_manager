import typing


class RegisterAccount(typing.NamedTuple('RegisterAccount', [('id', str), ('account_id', str), ('password', str)])):
    pass


class Login(typing.NamedTuple('Login', [('account_id', str), ('password', str)])):
    pass
