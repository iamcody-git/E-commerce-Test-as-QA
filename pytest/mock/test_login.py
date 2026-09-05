from login import login


def test_login(mocker):

    mocker.patch(
        "login.get_password",
        return_value="admin123"
    )

    result = login()

    assert result == "Login successful"