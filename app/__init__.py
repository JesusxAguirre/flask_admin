from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from .routes import login_manager, auth_scope
from .models.User import db

#from .routes import global_scope, api_scope, errors_scope

app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
app.config.from_object(Config)



#registrando el modulo de auth
app.register_blueprint(auth_scope, url_prefix="/")

#instanciando base de datos
db.init_app(app)

#instacioando login manager
login_manager.init_app(app)

#creando tablas
@app.before_first_request
def create_table():
    db.create_all()



