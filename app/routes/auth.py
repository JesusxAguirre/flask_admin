from flask import Blueprint, render_template
from flask_login import current_user, login_user, logout_user, login_required,LoginManager
from ..models.User import User



auth_scope = Blueprint("auth",__name__)
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) 



@auth_scope.get("/", methods=["GET","POST"])
def login_get():

    if current_user.is_authenticated:
        return "usuario auntenticado"

    return render_template("auth/login.html")

@auth_scope.post("/")
def login_post():

    return "aun no se crea el registro"


@auth_scope.get("/register")
def register_get():

    return render_template("auth/register.html")

@auth_scope.post("/register")
def register_post():


    return "envio de formulario"



@auth_scope.route("/logout")
@login_required
def logout():
    logout_user()

    return "Has cerrado sesion"