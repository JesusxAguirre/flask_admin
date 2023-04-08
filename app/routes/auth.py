from flask import Blueprint, render_template, request
from flask_login import current_user, login_user, logout_user, login_required, LoginManager
from ..models.User import User
from ..controller import user_controller


auth_scope = Blueprint("auth", __name__)
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

    if request.method == "POST":

        email = request.form['email']
        password = request.form['password']

        print(request.form)

        user = User(email = email, password = password)

        response =user_controller.login(user)


        return response,200



@auth_scope.get("/register")
def register_get():

    return render_template("auth/register.html")


@auth_scope.post("/register")
def register_post():

    if request.form['name']:

        name = request.form['name']
        apellido = request.form['apellido']
        email = request.form['email']
        password = request.form['password']

        

        user = User(name=name,
                    apellido=apellido,
                    email=email,
                    password=password)

        response = user_controller.create(user)

        return response, 200
    
    #validar que el email no exista en la BD
    if request.form['email_exist']:

        email = request.form['email_exist']

        
        return response
