from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required, LoginManager
from ..models.User import User
from ..controller import user_controller


auth_scope = Blueprint("auth", __name__)
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@auth_scope.get("/")
def login_get():

    if current_user.is_authenticated:
        
        return "usuario auntenticado"
    
   
    return render_template("auth/login.html")


@auth_scope.post("/")
def login_post():

    if request.method == "POST":
        print(request.form)

        email = request.form['email']
        password = request.form['password']
        remember = request.form['remember_me']



        user = User(email = email, password = password)

        _user =user_controller.login(user)

        login_user(_user,remember)
       

        return {"msj": "has iniciado sesion correctamente", "status_Code": 200 ,"url": url_for("security.dashboard_get")},200


auth_scope.get("/logout")
@login_required
def logout():
    logout_user()

    return redirect(url_for("auth.login_get"))


@auth_scope.get("/register")
def register_get():
   
   
    return render_template("auth/register.html")


@auth_scope.post("/register")
def register_post():

    if request.method == "POST":

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
    
    
