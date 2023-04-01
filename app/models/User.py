from flask_login import UserMixin, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from __init__ import db

login_manager = LoginManager()
    
class User(db.Model,UserMixin):

    __tablename__ = "user"

    id = db.Column(db.integer(),primary_key=True)
    name = db.Column(db.String(12))
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
