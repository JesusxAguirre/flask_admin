from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required, LoginManager
from ..models.User import User
from ..controller import user_controller
from ..models import Mail

auth_scope = Blueprint("auth", __name__)
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@auth_scope.route("/", methods=["GET"])
def login_get():

    if current_user.is_authenticated:

        return redirect(url_for('security.dashboard_get'))

    return render_template("auth/login.html")


@auth_scope.route("/", methods=["POST"])
def login_post():

    if request.method == "POST":

        email = request.form['email']
        password = request.form['password']

        # Verificar si la casilla de verificación "Recuérdame" está seleccionada
        if 'remember_me' in request.form:
            remember = True
        else:
            remember = False

        user = User(email=email, password=password)

        _user = user_controller.login(user)

        login_user(_user, remember, duration=None)

        return {"msj": "has iniciado sesion correctamente", "status_Code": 200, "url": url_for("security.dashboard_get")}, 200


# REGISTRO DE USUARIO REDERIZAR PAGINA
@auth_scope.route("/register", methods=["GET"])
def register_get():

    return render_template("auth/register.html")

# REGISTRO DE USUARIO ENVIO DE FORMULARIO


@auth_scope.route("/register", methods=["POST"])
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

# RECUPERAR CONTRASEÑA GET


@auth_scope.route("/forgot_password", methods=["GET"])
def recuperar_password_get():

    return render_template("auth/forgot.html")

# RECUPERAR CONTRASEÑA POST


@auth_scope.route("/forgot_password", methods=["POST"])
def recuperar_password_post():

    
    if 'tokenCorreo' in request.form:
        print("enra en el if de tokenCorreo")
        email = request.form['email']
        token_correo = request.form['tokenCorreo']

        user_ = User(email=email, )

        user_ = user_controller.get_by_email(user_)

        user_.token_correo = token_correo

        response=user_controller.forgot_password(user_)
        
        print(response.to_dict())

        return {"msj":"Nueva clave enviada al correo", "status_code":200, "usuario":  response.to_dict()},200

    email = request.form['email']

    user = User(email=email)

    user_ = user_controller.get_by_email(user)

    Mail.send_code_password(user_)

    return {"msj": "se envia correctamente"}, 200


# CERRAR SESION
@auth_scope.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()

    return redirect(url_for("auth.login_get"))
