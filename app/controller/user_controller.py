from ..models.User import User
from ..helpers import helpers




def create(user: User):
    user.email=helpers.sanitizar_caracteres(user.email)
    user.name = helpers.sanitizar_caracteres(user.name)
    user.apellido = helpers.sanitizar_caracteres(user.apellido)

    user = helpers.validate_users(user)
    return user.create(user)

def get_all():

    return User.get_all()

def  get_by_id(user : User)->User:

    return User.get_by_id(user.id)





#unica funcion que devuelve alfo diferente a un objeto usuario por ser el login
def login(user : User):

    _user = user.get_by_email(user)

    helpers.validate_login(_user,user.password)
    
    print(_user)
    return  _user



    