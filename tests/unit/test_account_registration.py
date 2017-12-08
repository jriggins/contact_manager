from contact_manager.account import handler, api, command
from contact_manager.account import reader
from contact_manager.account import repo
from contact_manager.account.model import example

def test_user1_can_register():
    repo_ = repo.InMemoryAccountRepository()
    api_ = api.Api(repo_)
    api_.register_account(command.RegisterAccount('user1@example.com', 'User1Password'))

    reader_ = reader.Reader(repo_)
    registered_user1 = reader_.find_user_by_email_address('user1@example.com')
    assert registered_user1


def test_user1_can_register_2():
    repo_ = repo.InMemoryAccountRepository()
    handler_ = handler.CommandHandler(repo_)
    handler_.register_account(command.RegisterAccount('user1@example.com', 'User1Password'))

    registered_user1 = repo_.find_user_by_email_address('user1@example.com')
    assert registered_user1



def test_user1_can_log_in_with_correct_user_name_and_password():
    repo_ = repo.InMemoryAccountRepository()
    # handler_ = handler.CommandHandler(repo_)
    # reader_ = reader.Reader(repo_)
    api_ = api.Api(repo_)
    api_.register_account(command.RegisterAccount('user1@example.com', 'User1Password'))

    logged_in_user1 = api_.login(command.Login('user1@example.com', 'User1Password'))
    assert logged_in_user1


def test_user1_can_log_in_with_correct_user_name_and_password_2():
    repo_ = repo.InMemoryAccountRepository()
    handler_ = handler.CommandHandler(repo_)
    handler_.register_account(command.RegisterAccount('user1@example.com', 'User1Password'))

    handler_.login(command.Login('user1@example.com', 'User1Password'))
    session = repo_.find_session_by_email_address('user1@example.com')
    assert session
