import os



class Config:


    DEBUG = True
    FLASK_DEBUG= False
    
    #CONFIGURACION DE EMAIL
    MAIL_SERVER= 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'quijess6@gmail.com'
    MAIL_PASSWORD = 'onebzquvinbjzbat'
    MAIL_DEFAULT_SENDER = 'quijess6@gmail.com'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True



    #VARIABLES DE BASE DE DATOS
    SECRET_KEY = "e23895acc525f92e886e9fe425046e0743855fbc038a70067540742c9fd34179"

    SQLALCHEMY_DATABASE_URI='postgresql://postgres:admin123@localhost:5432/flask-app-post'

    SQLALCHEMY_TRACK_MODIFICATION= False

    #SOBREESCRIBIENDO RUTAS DE FLASK

    TEMPLATE_FOLDER= "views/templates"
    STATIC_FOLDER = "views/static"