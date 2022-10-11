"""
Ana Helena A. C. R. Marcacini
        RA: 20.01305-0
"""
class User():
    def __init__(self, name, email, password):
        self._name = name
        self._email = email
        self._password = password
    def __str__(self) -> str:
        return f'User(name:{self._name}, email:{self._email}, password:{self._password})'