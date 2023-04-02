from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import select
from flask_sqlalchemy import SQLAlchemy
from ..models.exceptions import UserAlreadyExist


db = SQLAlchemy()

    
class User(db.Model,UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(12))
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


    def create(self,User : object):
        if self.user_exist(User):
            raise UserAlreadyExist(f"El email: {User.email} ya existe en la bd")
        
        db.session.add(User)
        db.session.commit()

        return True

    def update(self):
        pass

    def delete(self):
        pass
    
    def get_all(self):  

        return User.query.all()


    def get_by_id(self,User):
        pass

    def user_exist(self,User: object):

       return bool(db.execute(User.query.filter_by(email = User.email).first()))


