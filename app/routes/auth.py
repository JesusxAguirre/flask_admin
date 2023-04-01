from flask import Blueprint, render_template




auth_scope = Blueprint("views",__name__)






@auth_scope.route("/", methods=["GET","POST"])
def login():
 

    return render_template("login.html")

