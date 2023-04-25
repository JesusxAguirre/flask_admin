from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from .routes import login_manager, auth_scope, errors_scope,security_scope, users_scope
from .models.User import db
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
app.config['MAIL_SERVER']= Config.MAIL_SERVER
app.config['MAIL_PORT'] = Config.MAIL_PORT
app.config['MAIL_USERNAME'] = Config.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = Config.MAIL_PASSWORD
app.config['MAIL_USE_TLS'] = Config.MAIL_USE_TLS
app.config['MAIL_USE_SSL'] = Config.MAIL_USE_SSL
app.config.from_object(Config)

#creando token crsf
csrf = CSRFProtect(app)

#registrando el modulo de auth
app.register_blueprint(auth_scope, url_prefix="/")
app.register_blueprint(errors_scope, url_prefix="/")
app.register_blueprint(security_scope, url_prefix="/admin")
app.register_blueprint(users_scope, url_prefix="/users")

#instanciando base de datos
db.init_app(app)

#instacioando login manager
login_manager.init_app(app)

#instanciando token
csrf.init_app(app)

#creando tablas
@app.before_first_request
def create_table():
    db.create_all()



