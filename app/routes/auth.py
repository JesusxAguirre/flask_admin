from flask import Blueprint, render_template
from flask_login import current_user, login_user, logout_user, login_required



auth_scope = Blueprint("views",__name__)





@auth_scope.route("/", methods=["GET","POST"])
def login():

    if current_user.isaunthenticated:
        return "usuario auntenticado"

    return render_template("login.html")


@auth_scope.route("/register")
@login_required
def register():

    return "Sitio prohibido"