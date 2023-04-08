from ..models.User import User
from ..models.exceptions import InvalidadData, UserAlreadyExist, UserNotExist
import re

regex_email = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

regex_password = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,12}$"

regex_strings= r"^[a-zA-Z]{3,12}$"

regex_numeros= r"^[0-9]{3,12}$"


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
         raise InvalidadData(f"algo esta equivocado en la clave o el usuario")
     
    

def validate_user_already_exist_create(boleana : bool) -> None:
    print("ENTRA EN LA FUNCION USER ALREADY EXIST CREATE")
    if boleana:
        print("ENTRA EN EL IF FUNCION USER ALREADY EXIST CREATE")
        raise UserAlreadyExist(f"El email  ya existe en la bd")


def validate_user_already_exist_login(boleana : bool)->None:
   
    if boleana is False:
        raise  UserNotExist(f"El email no existe en la bd")
    


#VALIDACIONES REUTILIZABLES
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



