from contact_manager.account import api, command, repo

def test_user1_can_register():
    repo_ = repo.InMemoryAccountRepository()
    api_ = api.Api(repo_)
    api_.register_account(command.RegisterAccount('user1@example.com', 'User1Password'))

    registered_user1 = repo_.find_by_email_address('user1@example.com')
    assert registered_user1


def test_user1_can_log_in_with_correct_user_name_and_password():
    repo_ = repo.InMemoryAccountRepository()

    api_ = api.Api(repo_)
    api_.register_account(command.RegisterAccount('user1@example.com', 'User1Password'))

    logged_in_user1 = api_.login(command.Login('user1@example.com', 'User1Password'))
    assert logged_in_user1
