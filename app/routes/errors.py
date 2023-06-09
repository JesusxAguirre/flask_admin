from flask import Blueprint, Response, render_template
from ..models.exceptions import UserAlreadyExist,InvalidadData, UserNotExist, RequestTimeOut


errors_scope = Blueprint("errors",__name__)



def __generate_error_response(error: Exception) -> Response:
    message = {
        "ErrorType": type(error).__name__,
        "Message": str(error)
    }

    return message

@errors_scope.app_errorhandler(UserAlreadyExist)
@errors_scope.app_errorhandler(UserNotExist)
def handler_user_already_exist(error: Exception)-> Response:
    response = __generate_error_response(error)
    response["status_code"] = 409
    return response,409

@errors_scope.app_errorhandler(InvalidadData)
def handler_invalid_data(error : InvalidadData)-> Response:
    response = __generate_error_response(error)
    response['status_code']= 422

    return response,422


@errors_scope.app_errorhandler(RequestTimeOut)
def handler_invalid_data(error : RequestTimeOut)-> Response:
    response = __generate_error_response(error)
    response['status_code']= 408

    return response,408

@errors_scope.app_errorhandler(403)
def handler_invalid_permision(error):

    return render_template("error_unauthorized.html"),403

