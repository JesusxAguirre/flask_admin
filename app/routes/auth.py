from flask import Blueprint, render_template
from flask_login import current_user, login_user, logout_user, login_required,LoginManager
from ..models.User import User



auth_scope = Blueprint("auth",__name__)
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) 



@auth_scope.route("/", methods=["GET","POST"])
def login():

    if current_user.is_authenticated:
        return "usuario auntenticado"

    
    #user = User.query.filter_by(email="quijess6@gmail.com").first()
    #login_user(user)

    return render_template("auth/login.html")


@auth_scope.route("/register")
@login_required
def register():

    return "Sitio prohibido"

@auth_scope.route("/logout")
@login_required
def logout():
    logout_user()

    return "Has cerrado sesion"