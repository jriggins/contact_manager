from contact_manager.account import handler
from contact_manager.account import reader
from contact_manager.account import repo
from contact_manager.account.model import example

def test_user1_can_register():
    repo_ = repo.InMemoryAccountRepository()
    handler_ = handler.CommandHandler(repo_)
    reader_ = reader.Reader(repo_)

    registered_user1 = reader_.find_user_by_user_name('user1')
    assert not registered_user1

    user1 = example.get('user1')
    handler_.register_account(user1)

    registered_user1 = reader_.find_user_by_user_name('user1')
    assert registered_user1


def test_user1_can_log_in_with_correct_user_name_and_password():
    repo_ = repo.InMemoryAccountRepository()
    handler_ = handler.CommandHandler(repo_)
    reader_ = reader.Reader(repo_)
    user1 = example.get('user1')
    handler_.register_account(user1)

    logged_in_user1 = reader_.login('user1', 'User1Password')
    assert logged_in_user1
