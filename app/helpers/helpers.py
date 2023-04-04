from ..models.User import User
from ..models.exceptions import InvalidadData
import re

regex_email = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

regex_password = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$"

regex_strings= r"^[a-zA-Z]{3,12}$"

regex_numeros= r"^[0-9]{3,12}$"


def validate_users(user: User)->User:

    if not security_validation_email(user.email):

        raise InvalidadData(f"El email : {user.email} es invalido")

    if not security_validation_strings(user.name):
        raise InvalidadData(f"el nombre : {user.name} es invalido")
    
    if not security_validation_password(user.password):
        raise InvalidadData(f"la clave :{user.password} es invalida")
    
    return User(email = user.email, name = user.name, password = user.password)


def security_validation_email(email : str)-> bool:

    return bool(re.search(regex_email,email))


def security_validation_strings(cadena:str)-> bool:

    return bool(re.search(regex_strings,cadena))

def security_validation_numeros(numero : int)-> bool:

    return bool(re.search(regex_numeros,numero))

def security_validation_password(password : str)-> bool:

    return bool(re.search(regex_password,password))

def sanitizar_caracteres(string):

    return string.lower().strip()



