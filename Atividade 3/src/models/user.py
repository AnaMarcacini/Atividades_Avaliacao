"""
Ana Helena A. C. R. Marcacini
        RA: 20.01305-0
"""
class User():
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
    def __str__(self) -> str:
        return f'User(name:{self.name}, email:{self.email}, password:{self.password})'