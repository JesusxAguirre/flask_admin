from flask import Blueprint, Response
from ..models.exceptions import UserAlreadyExist


errors_scope = Blueprint("errors",__name__)



def __generate_error_response(error: Exception) -> Response:
    message = {
        "ErrorType": type(error).__name__,
        "Message": str(error)
    }

    return message

@errors_scope.errorhandler(UserAlreadyExist)
def handler_user_already_exist(error: UserAlreadyExist)-> Response:
    response = __generate_error_response(error)
    response.status_code = 409
    return response