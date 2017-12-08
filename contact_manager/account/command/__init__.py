import typing


class RegisterAccount(typing.NamedTuple('RegisterAccount', [('email_address', str), ('password', str)])):
    pass


class Login(typing.NamedTuple('Login', [('email_address', str), ('password', str)])):
    pass
