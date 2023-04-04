from flask import Blueprint, render_template, request
from flask_login import current_user, login_user, logout_user, login_required,LoginManager
from ..models.User import User
from ..controller import user_controller



auth_scope = Blueprint("auth",__name__)
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) 



@auth_scope.get("/")
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

    if request.method == "POST":

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        print(request.form)

        user =User(name=name,email=email)

        user.set_password(password)
        
        response = user_controller.create(user)

        return response
    


@auth_scope.route("/logout")
@login_required
def logout():
    logout_user()

    return "Has cerrado sesion"