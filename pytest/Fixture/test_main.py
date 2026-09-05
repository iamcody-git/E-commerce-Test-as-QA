import pytest
from main import UserManager

@pytest.fixture
def user_manager():
    ''' Create a fresh instance of usermanager before each test'''
    return UserManager()


def test_add_user(user_manager):
    assert user_manager.add_user("cody", "cody@gmail.com") == True
    assert user_manager.get_user("cody") == "cody@gmail.com"

def test_add_duplicate_user(user_manager):
    user_manager.add_user("cody", 'cody@gmail.com')
    with pytest.raises(ValueError):
        user_manager.add_user("cody", "c@gmail.com")
