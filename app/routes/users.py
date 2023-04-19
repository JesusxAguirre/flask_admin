from flask import Blueprint, render_template, request, redirect, url_for, jsonify, abort
from flask_login import current_user, login_required
from ..models.User import User
from ..controller import user_controller
from babel.dates import format_datetime



users_scope = Blueprint("users", __name__)



@users_scope.route("/usuarios", methods=["GET"])
@login_required
def users_list():
    if current_user.rol != "admin":
        abort(403)

    users = user_controller.get_all()
   
    users = [{'id': user.id, 'name': user.name, 'apellido':user.apellido, 'email': user.email} for user in users]

    return users,200


@users_scope.route("/", methods=["GET"])
@login_required
def users_get():

    if current_user.rol != "admin":
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


    #instacia de objeto usuario
    user = User(id = id_)

    #pasando instancia de objeto usuario el cual tambien devuelve una instancia 
    user_new = user_controller.get_by_id(user)

    #creando un diccionario con __dict__
    user_new = user_new.__dict__

    #eliminando del diccionario esa posicion del
    del user_new['_sa_instance_state']
    
    user_new['fecha_registro'] = format_datetime(user_new['fecha_registro'], locale='es_ES')
    return user_new, 200

