from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import select
from flask_sqlalchemy import SQLAlchemy
from ..models.exceptions import UserAlreadyExist, UserNotExist

from datetime import datetime

db = SQLAlchemy()


class User(db.Model, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12))
    apellido = db.Column(db.String(12))
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(20))
    fecha_registro = db.Column(db.Date(), default=datetime.utcnow)
    is_admin = db.Column(db.Boolean, default=False)
    rol = db.Column(db.String(30), default="Invitado")

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def create(self, User: object):
        if self.user_exist(User):
            raise UserAlreadyExist(f"El email  ya existe en la bd")

        db.session.add(User)
        db.session.commit()

        return {"msj": "Usuario registrado exitosamente", "status_code": 200}

    def update(self, user: object) -> dict:
        """funcion que actualiza los datos del usuario segun los datos enviados

        Args:
            user (object): objeto de tipo usuario

        Returns:
            dict: msj de respuesta que se debe enviar a la vista siempre y 
            cuando no haya una excepcion
        """

        # Obtener el usuario existente en la base de datos
        existing_user = User.query.filter_by(id=user.id).first()

        if existing_user is None:
            raise UserNotExist(
                f"El usuario {user.id} no existe en la base de datos")

        # Actualizar los atributos del usuario existente con los valores del objeto user, solo si son diferentes de None
        if user.name is not None:
            existing_user.name = user.name
        if user.apellido is not None:
            existing_user.apellido = user.apellido
        if user.email is not None:
            existing_user.email = user.email
        if user.password is not None:
            existing_user.password = user.password
        if user.telefono is not None:
            existing_user.telefono = user.telefono
        if user.direccion is not None:
            existing_user.direccion = user.direccion
        if user.fecha_registro is not None:
            existing_user.fecha_registro = user.fecha_registro
        if user.is_admin is not None:
            existing_user.is_admin = user.is_admin
        if user.rol is not None:
            existing_user.rol = user.rol

        db.session.commit()  # Realizar el commit para guardar los cambios en la base de datos

        return {"msj": "Datos del usuario modificado correctamente", "status_Code": 200}

    def delete(self):
        pass

    def get_all():
        #page = db.paginate(db.select(User).order_by(User.name))

        



        return User.query.all()

    def get_by_id(self, user: object) -> object:
        """ retorna un objeto con datos del usuario

        Args:
            user (object): un objeto de tipo usuario con los datos 
            del usuario en este caso solo el id

        Raises:
            UserNotExist: excepcion si el usuario con el id pasado no existe

        Returns:
            object: retorna un objeto de tipo usuario ya que solo en las capas intenras solo se manejan objetos
        """

        user_ = User.query.filter_by(id=user.id).first()

        if user_ is None:
            raise UserNotExist(f"El usuario con id : {user.id} no existe")

        return user_

    def get_by_email(self, user):

        user_ = User.query.filter_by(email=user.email).first()
        
        
        if user_ is None:

            raise UserNotExist(f"el usuario con email {user.email} no existe")
        
        return user_

    def user_exist(self, _user: object) -> bool:

        return bool(User.query.filter_by(email=_user.email).first())


    def to_dict(self):

        return {
            "id": self.id,
            "name": self.name,
            "apellido": self.apellido,
            "email": self.email,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "fecha_registro": self.fecha_registro,
            "rol": self.rol
        }