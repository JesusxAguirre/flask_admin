from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required




security_scope = Blueprint("security", __name__)
