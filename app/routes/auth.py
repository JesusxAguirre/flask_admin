from flask import Blueprint, render_template, request
from flask_login import current_user

auth_scope = Blueprint("views/auth",__name__)



@auth_scope.route("/", methods=["GET","POST"])
def login():



    return render_template("views/auth/login.html")