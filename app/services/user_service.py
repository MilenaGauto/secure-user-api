users = []

def create_user(user):
    users.append(user)
    return user


def get_users():
    return users


def get_user_by_id(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return None


def get_user_by_email(email: str):
    for user in users:
        if user.email == email:
            return user
    return None


def update_user(user_id: int, updated_user):
    for index, user in enumerate(users):
        if user.id == user_id:
            users[index] = updated_user
            return updated_user
    return None


def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return True
    return False