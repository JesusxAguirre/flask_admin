from ..models.User import User
from ..helpers import helpers



def get_all():

    return User.get_all()

def  get_by_id(user : User)->User:

    helpers.validate_user_id(user.id)
    
    return user.get_by_id(user)

def create(user: User) -> User:
    user.email=helpers.sanitizar_caracteres(user.email)
    user.name = helpers.sanitizar_caracteres(user.name)
    user.apellido = helpers.sanitizar_caracteres(user.apellido)

    user = helpers.validate_users(user)
    return user.create(user)


def update(user: User)-> User:

    helpers.validate_user_update(user)

    return user.update(user)



#unica funcion que devuelve alfo diferente a un objeto usuario por ser el login
def login(user : User)-> User:

    _user = user.get_by_email(user)

    helpers.validate_login(_user,user.password)
    
    
    return  _user



    