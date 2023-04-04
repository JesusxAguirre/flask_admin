from ..models.User import User
from ..helpers import helpers




def create(user: User):
    user.email=helpers.sanitizar_caracteres(user.email)
    user.email = helpers.sanitizar_caracteres(user.name)
    
    helpers.security_validation_email(user.email)
    helpers.security_validation_password(user.password)
    helpers.security_validation_strings(user.name)

    user = User(email=user.email,name=user.name, password=user.password)

    return user.create(user)

def get_all():

    return User.get_all(User)

def  get_by_id(user : User)->User:

    return User.get_by_id(user.id)