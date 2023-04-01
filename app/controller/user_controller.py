from ..models import User
from ..helpers import helpers




def create(user_: User)-> User:
    User.email=helpers.sanitizar_caracteres(User.email)
    User.email = helpers.sanitizar_caracteres(User.name)
    
    helpers.security_validation_email(User.email)
    helpers.security_validation_password(User.password)
    helpers.security_validation_strings(User.name)


    return User.create(User)

def get_all()->User:

    return User.get_all(User)

def load_user(user_ : User):

    return load_user(User)