from flask import Blueprint, render_template, request
from flask_login import current_user

auth_scope = Blueprint("views/auth",__name__)



@auth_scope.route("/", methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return "Este usuario ya esta registrado"


    return render_template("auth/login.html")