from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import  LoginManager


login_manager = LoginManager()

db = SQLAlchemy()

#from .routes import global_scope, api_scope, errors_scope

app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
app.config.from_object(Config)

db.init_app(app)
login_manager.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

#app.register_blueprint(global_scope, url_prefix="/")
