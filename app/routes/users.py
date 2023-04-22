from flask import Blueprint, render_template, request, redirect, url_for, jsonify, abort
from flask_login import current_user, login_required
from ..models.User import User
from ..controller import user_controller
from babel.dates import format_datetime


users_scope = Blueprint("users", __name__)


@users_scope.route("/usuarios", methods=["GET"])
@login_required
def users_list():
    if current_user.rol not in ['admin', 'gerente']:
        abort(403)

    users = user_controller.get_all()

    users = [ user.to_dict() for user in users]

    return users, 200


@users_scope.route("/", methods=["GET"])
@login_required
def users_get():

    if current_user.rol not in ['admin', 'gerente']:
        abort(403)

    return render_template("users/users.html")


@users_scope.route("/<id_>", methods=["GET"])
@login_required
def users_get_details(id_):
    """funcion que devuelve un usuario por url

    Args:
        id_ (entero): id del usuario

    Returns:
        un diccionario: diccionario con datos del usuario requerido
    """

    if current_user.rol not in ['admin', 'gerente']:
        abort(403)

    # instacia de objeto usuario
    user = User(id=id_)

    # pasando instancia de objeto usuario el cual tambien devuelve una instancia
    user_new = user_controller.get_by_id(user)

    # creando un diccionario con __dict__
    user_new = user_new.__dict__

    # eliminando del diccionario esa posicion del
    del user_new['_sa_instance_state']

    # formateando la fecha a formato castellano
    user_new['fecha_registro'] = format_datetime(
        user_new['fecha_registro'], locale='es_ES')

    user_new['fecha_registro'] = user_new['fecha_registro'].split(',')[
        0].strip()

    return user_new, 200


@users_scope.route("/<id_>", methods = ["PUT"])
@login_required
def users_update(id_):
    """funcion que actualiza el rol de un usuario

    Args: id del usuario que se quiere actualizar

    Returns:
        dictionary: diccionario con respuesta de la solicitud
    """

    print("ENTRA EN LA FUNCION DE PUT")

    if current_user.rol not in ['admin', 'gerente']:
        abort(403)

    rol = request.form['roles']

    user = User(rol= rol, id = id_)

    user_actualizado =user_controller.update(user)


    print(current_user.id)
    print(id_)

    if str(current_user.id) == str(id_) :
        
        return {
            "msj": "Has editado correctamente tu usuario",
            "status_code": 200,
            "url": url_for("auth.logout")},200


    return user_actualizado.to_dict(),200