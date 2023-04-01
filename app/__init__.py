from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

from .routes import auth_scope

#login_manager = LoginManager()

db = SQLAlchemy()

#from .routes import global_scope, api_scope, errors_scope

app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
app.config.from_object(Config)

#instaciando la base de datos
db.init_app(app)
#instanciando la clase de login manager y sus atributos


#creando la tabla suponiendo que no exista
@app.before_first_request
def create_table():
    db.create_all()


#registrando el modulo de auth
app.register_blueprint(auth_scope, url_prefix="/")

#app.register_blueprint(global_scope, url_prefix="/")
