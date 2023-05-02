from ..models.User import User
from ..helpers import helpers
from ..models.Mail import generate_code, send_message_restore


def get_all():

    return User.get_all()

def  get_by_id(user : User)->User:

    helpers.validate_user_id(user.id)
    
    return user.get_by_id(user)

def get_by_email(user_ : User)-> User:

    
    user_.email = helpers.sanitizar_caracteres(user_.email)

    return user_.get_by_email(user_)


def create(user: User) -> User:
    user.email=helpers.sanitizar_caracteres(user.email)
    user.name = helpers.sanitizar_caracteres(user.name)
    user.apellido = helpers.sanitizar_caracteres(user.apellido)

    user = helpers.validate_users(user)
    return user.create(user)


def update_rol(user: User)-> User:

    user.id = helpers.sanitizar_caracteres(user.id)
    user.rol = helpers.sanitizar_caracteres(user.rol)

    helpers.validate_user_update_rol(user)

    return user.update(user)

def update(user_ : User)-> User:

    user_.id = helpers.sanitizar_caracteres(user_.id)
    user_.name = helpers.sanitizar_caracteres(user_.name)
    user_.apellido = helpers.sanitizar_caracteres(user_.apellido)
    user_.email = helpers.sanitizar_caracteres(user_.email)
    user_.telefono = helpers.sanitizar_caracteres(user_.telefono)
    user_.password = helpers.sanitizar_caracteres(user_.password)
    user_.fecha_nacimiento = helpers.sanitizar_caracteres(user_.fecha_nacimiento)
    user_.direccion = helpers.sanitizar_caracteres(user_.direccion)

    helpers.validate_user_update(user_)

    return user_.update(user_)


def forgot_password(user_: User)-> User:

    user_.email = helpers.sanitizar_caracteres(user_.email)
    user_.token_correo = helpers.sanitizar_caracteres(user_.token_correo)

    print("ESTE ES E;L VALOR DEL TOKEN DE CORREO VERIFICARE QUE SEA UN STRING")
    print(user_.token_correo)

    helpers.validate_expirated_code()

    helpers.validate_forgot_password(user_)

    password = generate_code()
    user_.set_password(password)

    #envio de correo con nueva clave
    send_message_restore(password)

    return user_.update(user_)


#unica funcion que devuelve alfo diferente a un objeto usuario por ser el login
def login(user : User)-> User:

    _user = user.get_by_email(user)

    helpers.validate_login(_user,user.password)
    
    
    return  _user



    