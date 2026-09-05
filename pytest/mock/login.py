def get_password():
    return "admin123"


def login():
    password = get_password()

    if password == "admin123":
        return "Login successful"

    return "Login failed"