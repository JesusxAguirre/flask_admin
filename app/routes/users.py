from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required




users_scope = Blueprint("users", __name__)


@users_scope.get("/")
@login_required
def users_get():

    return render_template("users/users.html")