from flask import session
from datetime import datetime
from ..models import User
from flask_mail import Mail, Message
from random import randint

mail = Mail()  # initialize Flask-Mail instance

def generate_code() -> str:
    code = ""
    for i in range(0, 6):
        code += str(randint(0, 9))
    return code

def send_code_password(user_: User) -> None:
    code = generate_code()
    session['code'] = code
    session['code_created_at'] = datetime.now()
    session['email_en_recuperacion'] = user_.email
    msg = Message(subject="Password Recovery Code", recipients=[user_.email])
    msg.body = f"Dear {user_.name},\n\nYour password recovery code is: {code}\n\nPlease enter this code on the password recovery page to reset your password.\n\nBest regards,\nThe Password Recovery Team"
    mail.send(msg)

