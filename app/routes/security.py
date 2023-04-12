from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required




security_scope = Blueprint("security", __name__)


@security_scope.route("/", methods=["GET"])
@login_required
def dashboard_get():

    return render_template("admin/dashboard.html")