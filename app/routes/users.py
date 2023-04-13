from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_login import current_user, login_required
from ..models.User import User
from ..controller import user_controller



users_scope = Blueprint("users", __name__)


@users_scope.route("/", methods=["GET"])
@login_required
def users_get():
    users = user_controller.get_all()
   
    users = [{'id': user.id, 'name': user.name, 'email': user.email} for user in users]
    

    return render_template("users/users.html",users=users)

@users_scope.route("/usuarios", methods=["GET"])
@login_required
def users_list():

    users = user_controller.get_all()
   
    users = [{'id': user.id, 'name': user.name, 'email': user.email} for user in users]

    return users,200
