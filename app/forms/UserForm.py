from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, Regexp, InputRequired



class LoginForm(FlaskForm):

    email = StringField(
        "email",
        validators=[DataRequired("Este campo no puede estar vacio"),
                    Email("Digita un email valido")])

    password = PasswordField(
        "password",
        validators=[DataRequired("Este campo no puede estar vacio"),
                    Length(min=8,max=12)]
    )

    remember_me = BooleanField("Recuerdame")

    submit = SubmitField("iniciar_sesion")


class RegistroForm(FlaskForm):
    usuario = StringField(
        "usuario",
        validators=[DataRequired(message="No puedes dejar este campo vacio"),
                    Email(message="Escribe un email valido")])

    password = PasswordField(
        "password",
        validators=[DataRequired(message="No puedes dejar este campo vacio"),
                    Regexp(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$',message="La contraseña debe contener una mayuscula una minuscula un numero y un caracter especial [@$!%*?&]"),
                    Length(min=8,max=12)]
    )

    nombre = StringField('nombre', validators=[
        InputRequired(message="Este campo no puede estar vacio"),
        Regexp(r'^[a-zA-Z]+$', message='Solo se permiten letras'),
        Length(min=3, max=12, message='La longitud debe estar entre 3 y 12 caracteres')
    ])

    submit = SubmitField("registrar usuario")
