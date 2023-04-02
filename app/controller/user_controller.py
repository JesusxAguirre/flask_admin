from ..models import User
from ..helpers import helpers




def create(user: User)-> User:
    user.email=helpers.sanitizar_caracteres(user.email)
    user.email = helpers.sanitizar_caracteres(user.name)
    
    helpers.security_validation_email(user.email)
    helpers.security_validation_password(user.password)
    helpers.security_validation_strings(user.name)


    return User.create(User)

def get_all()->User:

    return User.get_all(User)

def  get_by_id(user : User)->User:

    return User.get_by_id(user.id)