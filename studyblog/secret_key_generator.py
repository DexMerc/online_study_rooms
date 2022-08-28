import secrets


def generate_key():
    length = 50
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

    return ''.join(secrets.choice(chars) for i in range(length))
