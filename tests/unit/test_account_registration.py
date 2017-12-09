import jwt
import pytest

from contact_manager.account import api, command, repo


@pytest.fixture()
def session_secret():
    return 'as;lkdjaskl;jf'

@pytest.fixture()
def api_(session_secret):
    repo_ = repo.InMemoryAccountRepository()
    return api.Api(repo_, session_secret)


def test_user1_can_register(api_):
    api_.register_account(command.RegisterAccount('123', 'user1@example.com', 'User1Password'))

    registered_user1 = api_._repo.find_by_email_address('user1@example.com')
    assert registered_user1


def test_user1_can_log_in_with_correct_user_name_and_password(api_, session_secret):
    api_.register_account(command.RegisterAccount('123', 'user1@example.com', 'User1Password'))

    logged_in_user1 = api_.login(command.Login('user1@example.com', 'User1Password'))
    assert jwt.decode(logged_in_user1, session_secret) == dict(id='123')

