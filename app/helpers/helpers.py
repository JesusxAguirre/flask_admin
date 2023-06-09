from ..models.User import User
from ..models.exceptions import InvalidadData, UserAlreadyExist, UserNotExist, RequestTimeOut
import re
from datetime import timedelta, datetime
import pytz
import time
from flask import session

# Establecer la zona horaria local
local_tz = pytz.timezone('America/Caracas')

regex_email = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

regex_password = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,12}$"

regex_strings= r"^[a-zA-Z]{3,12}$"

regex_telefono= r"^04\d{9}$"

regex_numeros= r"^[0-9]{3,12}$"

regex_fecha = r"^\d{4}-\d{2}-\d{2}$"

#VALIDACION DEL OBJETO USUARIO - CREATE
def validate_users(user: User)->User:

    if not security_validation_email(user.email):

        raise InvalidadData(f"El email : {user.email} es invalido")
        
    if not security_validation_strings(user.name):
        raise InvalidadData(f"el nombre : {user.name} es invalido")
    
    if not security_validation_strings(user.apellido):
        raise InvalidadData(f"el apellido : {user.apellido} es invalido")
    
    if not security_validation_password(user.password):
        raise InvalidadData(f"la clave :{user.password} es invalida")
    
    _user = User(email = user.email, name = user.name, apellido = user.apellido)

    _user.set_password(user.password)

    return _user


def validate_login(user : User, password : str) -> None:

     if user is None or user.check_password(password) is False:
        print(user.password)
        print(password)
        raise InvalidadData(f"algo esta equivocado en la clave o el usuario")
     
    

def validate_user_already_exist_login(boleana : bool)->None:
   
    if boleana is False:
        raise  UserNotExist(f"El email no existe en la bd")
    
def validate_user_id(id_ : str)-> None:
    """validando que la id sea entero con una excepcion

    Args:
        id_ (int): id de usuario

    Returns:
        None: no retorna nada
    """


    if not id_.isdigit():
        raise InvalidadData(f"estas enviando un id que no es de tipo numerico")

def validate_user_update_rol(user: User)-> None:

    if not user.id.isdigit():
        raise InvalidadData(f"Estas envindo un id que no es de tipo numerico")

    if user.rol not in ["almacenista","Invitado","admin","vendedora","gerente"]:
        raise InvalidadData(F"Estas enviando un rol que no existe en la BD")


def validate_user_update(user_: User)-> None:

    if not user_.id.isdigit():
        raise InvalidadData(f"Estas enviando un id que no es de tipo numerico")

    if user_.name is not None:
        if not security_validation_strings(user_.name):
            raise InvalidadData(f"el nombre : {user_.name} es invalido")
        
    if user_.apellido is not None:
        if not security_validation_strings(user_.apellido):
            raise InvalidadData(f"el apellido : {user_.apellido} es invalido")

    if user_.email is not None:
        if not security_validation_email(user_.email):

            raise InvalidadData(f"El email : {user_.email} es invalido")
   
    if user_.telefono is not None:
        if not security_validation_telefono(user_.telefono):

            raise InvalidadData(f"el telefono : {user_.telefono} es invalido")    
    
    if user_.password is not None and user_.password is not "":
        if not security_validation_password(user_.password):
            raise InvalidadData(f"la clave :{user_.password} es invalida")
    
    if user_.fecha_nacimiento is not None:
  
        if not security_validation_fecha(user_.fecha_nacimiento):
            raise InvalidadData(f"la fecha de nacimiento : {user_.fecha_nacimiento} es invalida")
    
    if user_.direccion is not None:
        if not security_validation_strings(user_.direccion):
            raise InvalidadData(f"la direccion: {user_.direccion} es invalida")

def validate_expirated_code() -> None:
    """funcion que valida si el codigo ya expiro

    Raises:
        RequestTimeOut: excepcion para darle una respuesta a l usuario cuando envia el formulario
        RequestTimeOut: excepcion para darle una respuesta a l usuario cuando envia el formulario
    """

    if not 'code_created_at' in session:
        raise RequestTimeOut(f"El codigo de recuperacion expiro")

    if datetime.now(local_tz) > session['code_created_at'] + timedelta(minutes=5):
            # La variable de sesión ha expirado
            del session['code']
            del session['code_created_at']
            del session['email_en_recuperacion']

            raise RequestTimeOut(f"El codigo de recuperacion expiro")
            


#VALIDAR QUE LOS DATOS ENVIADOS PARA RESETEAR LA CONTRASEÑA SEAN VALIDOS            
def validate_forgot_password(user_ : User)-> None:
    """Validacion de los campos del envio de validacion de contraseña
    es decir se valida que no se hayan enviado datos invalidos.

    Args:
        user_ (User): objeto de tipo usuario

    Raises:
        InvalidadData: _description_
        InvalidadData: _description_
        InvalidadData: _description_
    """

    if not security_validation_email(user_.email):

        raise InvalidadData(f"El email : {user.email} es invalido")

    if not user_.token_correo.isdigit():

        raise InvalidadData(f"el token no es un dato numerico algo esta equivocado")

    if user_.token_correo != session['code']:
        
        raise InvalidadData(f"El token enviado no es el correcto por favor escribalo correctamente")

#VALIDACIONES REUTILIZABLES
def security_validation_email(email : str)-> bool:

    return bool(re.search(regex_email,email))


def security_validation_strings(cadena:str)-> bool:

    return bool(re.search(regex_strings,cadena))

def security_validation_numeros(numero : int)-> bool:

    return bool(re.search(regex_numeros,numero))

def security_validation_password(password : str)-> bool:

    return bool(re.search(regex_password,password))

def security_validation_telefono(telefono : str)-> bool:

    return bool(re.search(regex_telefono, telefono))

def security_validation_fecha(fecha)->bool:

    return bool(re.search(regex_fecha, fecha))    

def sanitizar_caracteres(string):
    string =string.lower().strip()
    
    if string == "none" or string == "" or string is None:
        return None
    else:
        return string

