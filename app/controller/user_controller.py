from ..models.User import User
from ..helpers import helpers




def create(user: User):
    user.email=helpers.sanitizar_caracteres(user.email)
    user.name = helpers.sanitizar_caracteres(user.name)
    user.apellido = helpers.sanitizar_caracteres(user.apellido)

    user = helpers.validate_users(user)
    return user.create(user)

def get_all():

    return User.get_all(User)

def  get_by_id(user : User)->User:

    return User.get_by_id(user.id)





#unica funcion que devuelve alfo diferente a un objeto usuario por ser el login
def login(user : User)-> User:

    _user = user.get_by_email(user)

    helpers.validate_login(_user,user.password)
    

    return  {"msj": "has iniciado sesion correctamente", "status_Code": 200}


def user_already_exist_create(user: User) -> None:

    helpers.validate_user_already_exist_create(user.user_exist(user))


    return {"msj": "el email no existe en la bd", "status_code":200}
    